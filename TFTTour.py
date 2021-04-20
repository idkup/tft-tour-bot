class TFTTour:
    def __init__(self, name: str, channel_ids: list):
        """Creates a new tournament object"""
        self._name = name
        self._log_channel_id = channel_ids[0]
        self._results_channel_id = channel_ids[1]
        self._scoring_channel_id = channel_ids[2]
        self._chat_channel_id = channel_ids[3]
        self._participants = []
