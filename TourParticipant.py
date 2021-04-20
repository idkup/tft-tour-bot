class TourParticipant:
    def __init__(self, discord_id: int, name: str):
        """Creates a new TourParticipant."""
        self._discord_id = discord_id
        self._name = name
        self._score = 0
        self._confirmed = False

    def get_discord_id(self) -> int:
        """Returns the participant's Discord ID."""
        return self._discord_id

    def get_name(self) -> str:
        """Returns the participant's name."""
        return self._name

    def get_score(self) -> int:
        """Returns the participant's current score."""
        return self._score

    def get_confirmed(self) -> bool:
        """Returns if the participant has confirmed their participation."""
        return self._confirmed

    def set_discord_id(self, discord_id: int):
        """Sets a new Discord ID for the participant."""
        self._discord_id = discord_id

    def set_name(self, name: str):
        """Sets a new name for the participant."""
        self._name = name

    def set_score(self, score: int):
        """Alters the participant's score."""
        self._score = score

    def set_confirmed(self, confirmed: bool):
        """Sets the participant's confirmation status."""
        self._confirmed = confirmed