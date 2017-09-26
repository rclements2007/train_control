"""
Copyright Ryan Clements

Class definition for a single train
"""


class Train:
    """
    class description: Fill in later
    """
    def __init__(self, serial_number, line, train_length,
                 current_track_section):

        # Real Time Train Status and Position
        self.current_speed = None
        self.track_section_speed_limit = None
        self.line = line
        self.current_track_section = current_track_section
        self.last_seen_position_sensor = None

        # Static Train configuration
        self.train_length = train_length
        self.serial_number = serial_number

    def start_service(self):
        """ Public method to place a train into service

        This method is called by this trains control system to initialize the
        train and place it into service. It is responsible for performing a
        systems check and deciding whether or no the train is fit for service.
        If it is, the method will spawn a new service thread and return.

        Returns:
            bool: Return value. True if service loop started, False otherwise

        """
        pass

    def remove_from_service(self):
        """ Public method to remove the train from service

        This method is called by the central control to remove a train from
        service. The train will proceed to the next stop and halt service
        until placed back into service.
        """
        pass

    def emergency_stop(self):
        """ Public method to stop the train in an emergenc

        This is a public facing method which is to be called if the train
        needs to be stopped immediately. The halt condition will persist
        until the train is placed back into service or told to proceed in a
        degraded mode.
        """
        pass

    def proceed_degraded_mode(self):
        """ Public method informing the train to move slowly to the next station

        This is a public facing method which is to be called by the central
        control if the train needs to proceed in degraded mode. This method
        will slowly move (10mph or less) the train to the next station and halt
        all progress until the train is placed back into service.
        """
        pass

    def report_train_status(self):
        """ Public method returning the train status to central control

        Retrieves status data from this train and its cards, returning it
        to the caller.
        """
        pass

    def _service_loop(self):
        """ Private method performing all control and monitoring for service

        This method is designed to be called in its own thread where it will
        continuously monitor and control the train for all normal operations
        on the line until it is taken out of service.
        """
        pass

    def _open_doors(self):
        """ Private method to open all doors connected to this train

        This method loops through all of the cars connected to this
        train and signals them to open their doors.
        """
        pass

    def _close_doors(self):
        """ Private method to close all doors connected to this train

        This method loops through all of the cars connected to this
        train and signals them to close their doors.
        """
        pass
