from TourParticipant import TourParticipant


class TFTTour:
    def __init__(self, name: str, channel_ids: list, tour_role_id: int):
        """Creates a new tournament object"""
        self._name = name
        self._command_channel_id = channel_ids[0]
        self._log_channel_id = channel_ids[1]
        self._results_channel_id = channel_ids[2]
        self._scoring_channel_id = channel_ids[3]
        self._chat_channel_id = channel_ids[4]
        self._tour_role_id = tour_role_id
        self._participants = []
        self._phase = 0
        
    def get_name(self) -> str:
        """Returns the tournament's name."""
        return self._name

    def get_command_channel(self) -> int:
        """Returns the ID of the command channel."""
        return self._command_channel_id
    
    def get_log_channel(self) -> int:
        """Returns the ID of the log channel."""
        return self._log_channel_id
    
    def get_results_channel(self) -> int:
        """Returns the ID of the results channel."""
        return self._results_channel_id
    
    def get_scoring_channel(self) -> int:
        """Returns the ID of the scoring channel."""
        return self._scoring_channel_id

    def get_chat_channel(self) -> int:
        """Returns the ID of the chat channel."""
        return self._chat_channel_id

    def get_participants(self) -> list:
        """Returns a list of participants in the tournament."""
        return self._participants

    def get_current_phase(self) -> int:
        """Returns the current phase of the tournament."""
        return self._phase

    def get_tour_role(self) -> int:
        """Returns the ID of the tournament role."""
        return self._tour_role_id

    def add_participant(self, participant: TourParticipant):
        """Adds a TourParticipant object to the self._participants list."""
        self._participants.append(participant)

    def remove_participant(self, participant_id: int):
        """Removes a TourParticipant from self._participants based on their Discord ID."""
        for p in self._participants:
            if p.get_discord_id() == participant_id:
                self._participants.remove(p)
                break

    def set_phase(self, new_phase: int):
        """Sets the phase of the tournament."""
        self._phase = new_phase
