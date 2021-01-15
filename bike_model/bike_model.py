class BikeModel:
    
    def next_bike_user(self,mode: str) -> float:
        if mode not in ['start', 'end']:
            raise ValueError(f"mode should be 'start' or 'end', not {mode}")

        raise NotImplementedError
