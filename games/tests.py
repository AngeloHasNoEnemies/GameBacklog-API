from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Game


class GameModelTest(TestCase):
    """Test the Game model __str__ method."""

    def test_str_representation(self):
        game = Game(title="Elden Ring", platform="PC", status="Playing", hours_played=40)
        self.assertEqual(str(game), "Elden Ring (PC) – Playing")


class GameAPITest(APITestCase):
    """Test full CRUD and validation via the REST API."""

    def get_url(self, name, **kwargs):
        kwargs.setdefault('version', 'v1')
        return reverse(name, kwargs=kwargs)

    # ── 1. POST valid game → 201 Created ────────────────────────────────────
    def test_create_valid_game(self):
        url = self.get_url('game-list')
        data = {
            'title': 'Hollow Knight',
            'platform': 'PC',
            'status': 'Planned',
            'hours_played': 0,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 1)
        self.assertEqual(Game.objects.first().title, 'Hollow Knight')

    # ── 2. POST negative hours → 400 Bad Request ────────────────────────────
    def test_create_game_negative_hours(self):
        url = self.get_url('game-list')
        data = {
            'title': 'Cyberpunk 2077',
            'platform': 'PS5',
            'status': 'Playing',
            'hours_played': -5,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('hours_played', response.data)

    # ── 3. POST Finished with 0 hours → 400 Bad Request ─────────────────────
    def test_cannot_mark_finished_with_zero_hours(self):
        url = self.get_url('game-list')
        data = {
            'title': 'God of War',
            'platform': 'PS4',
            'status': 'Finished',
            'hours_played': 0,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # ── 4. POST Finished with hours > 0 → 201 Created ───────────────────────
    def test_create_finished_game_with_hours(self):
        url = self.get_url('game-list')
        data = {
            'title': 'The Last of Us',
            'platform': 'PS5',
            'status': 'Finished',
            'hours_played': 15,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # ── 5. GET list returns 200 ──────────────────────────────────────────────
    def test_list_games(self):
        Game.objects.create(title='Minecraft', platform='PC', status='Playing', hours_played=200)
        url = self.get_url('game-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ── 6. DELETE a game → 204 No Content ───────────────────────────────────
    def test_delete_game(self):
        game = Game.objects.create(
            title='Stardew Valley', platform='PC', status='Planned', hours_played=0
        )
        url = self.get_url('game-detail', pk=game.pk)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Game.objects.count(), 0)

    # ── 7. PATCH update status to Finished with hours → 200 ─────────────────
    def test_patch_game_to_finished(self):
        game = Game.objects.create(
            title='Sekiro', platform='PC', status='Playing', hours_played=50
        )
        url = self.get_url('game-detail', pk=game.pk)
        response = self.client.patch(url, {'status': 'Finished'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
