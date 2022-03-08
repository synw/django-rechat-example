from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

from rechat.models import ChatRoom


class Command(BaseCommand):
    help = "Initialize some chatrooms"

    def handle(self, *args, **options):
        print("Creating some demo chat rooms")
        print(" creating room 1: for users")
        ChatRoom.objects.get_or_create(name="Room 1", slug="room-1", level="users")
        print(" creating moderators group")
        g, _ = Group.objects.get_or_create(name="moderators")
        print(" creating moderators room")
        r, _ = ChatRoom.objects.get_or_create(
            name="Moderators", slug="moderators", level="group"
        )
        r.groups.add(g)
        print(" creating superuser room")
        ChatRoom.objects.get_or_create(
            name="Superuser", slug="superuser", level="superuser", save_messages=False
        )
        print("done")
