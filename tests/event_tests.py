import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import Event, Game, GameType, Gamer

class EventTests(APITestCase):
    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }
        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # SEED DATABASE WITH ONE GAME TYPE AND GAME
        # This is needed because the API does not expose a /gametypes
        # endpoint for creating game types
        gametype = GameType()
        gametype.label = "Board game"
        gametype.save()

        game = Game()
        game.gametype_id = 1
        game.skill_level = 5
        game.title = "Monopoly"
        game.maker = "Milton Bradley"
        game.number_of_players = 4
        game.gamer_id = 1

        game.save()


    def test_create_event(self):
        """
        Ensure we can create a new event
        """
        # define game properties
        url = "/events"
        data = {
            "time": "13:00",
            "date": "11-04-2020",
            "description": "Party Night",
            "organizer": 1,
            "gameId": 1
        }

        # make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # parse the JSON in the response body
        json_response = json.loads(response.content)

        # assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # assert that the properties on the created resource are correct
        self.assertEqual(json_response["time"], "13:00")
        self.assertEqual(json_response["date"], "11-04-2020")
        self.assertEqual(json_response["description"], "Party Night")
        
    def test_get_event(self):
        """
        Ensure we can get an existing event.
        """

        # Seed the database with an event
        event = Event()
        event.time = "13:00"
        event.date = "11-04-2020"
        event.description = "Party Night"

        gamer = Gamer.objects.get(pk=1)
        event.organizer = gamer

        game = Game.objects.get(pk=1)
        event.game = game

        event.save()

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.get(f"/events/{event.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["time"], "13:00")
        self.assertEqual(json_response["date"], "11-04-2020")
        self.assertEqual(json_response["description"], "Party Night")

    def test_change_event(self):
        """
        Ensure we can change an existing event.
        """
        event = Event()
        event.time = "13:00"
        event.date = "11-04-2020"
        event.description = "Party Night"

        gamer = Gamer.objects.get(pk=1)
        event.organizer = gamer

        game = Game.objects.get(pk=1)
        event.game = game

        event.save()

        # DEFINE NEW PROPERTIES FOR GAME
        data = {
            "time": "15:00",
            "date": "12-25-2020",
            "description": "Xmas Party Night",
            "organizer": 1,
            "gameId": 1
        }

        # print('GAME ID ' + str(game.id))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.put(f"/events/{event.id}", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # get game again to verify changes
        response = self.client.get(f"/events/{event.id}")
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # assert that the properties are correct
        self.assertEqual(json_response["time"], "15:00")
        self.assertEqual(json_response["date"], "12-25-2020")
        self.assertEqual(json_response["description"], "Xmas Party Night")

    def test_delete_event(self):
        """
        Ensure we can delete an existing event.
        """
        event = Event()
        event.time = "13:00"
        event.date = "11-04-2020"
        event.description = "Party Night"

        gamer = Gamer.objects.get(pk=1)
        event.organizer = gamer

        game = Game.objects.get(pk=1)
        event.game = game

        event.save()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.delete(f"/events/{event.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET GAME AGAIN TO VERIFY 404 response
        response = self.client.get(f"/events/{event.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)