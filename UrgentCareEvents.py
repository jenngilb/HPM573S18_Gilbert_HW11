from enum import Enum
import Parameters as P
import scr.DiscreteEventClasses as SimLib


class Priority(Enum):
    """ priority of urgent care simulation events (low number implies higher priority)"""
    ARRIVAL = 1
    END_OF_EXAM = 0
    CLOSE = 2


class Arrival(SimLib.SimulationEvent):
    def __init__(self, time, patient, urgent_care):
        """
        creates the arrival of the next patient event
        :param time: time of next patient's arrival
        :param patient: next patient
        :param urgent_care: the urgent care
        """
        # initialize the master class
        SimLib.SimulationEvent.__init__(self, time, Priority.ARRIVAL.value)

        self.patient = patient
        self.urgentCare = urgent_care

        # trace
        urgent_care.trace.add_message(
            str(patient) + ' will arrive at time {t:.{deci}f}.'.format(t=time, deci=P.DECI))

    def process(self):
        """ processes the arrival of a new patient """

        # trace
        self.urgentCare.trace.add_message(
            'Processing arrival of ' + str(self.patient) + '.')

        # receive the new patient
        self.urgentCare.receive_patient(self.patient)


class EndOfExam(SimLib.SimulationEvent):
    def __init__(self, time, exam_room, urgent_care):
        """
        create the end of service for an specified exam room
        :param time: time of the service completion
        :param exam_room: the exam room
        :param urgent_care: the urgent care
        """
        # initialize the base class
        SimLib.SimulationEvent.__init__(self, time, Priority.END_OF_EXAM.value)

        self.examRoom = exam_room
        self.urgentCare = urgent_care

        # trace
        urgent_care.trace.add_message(
            str(exam_room) + ' will finish service at time {t:.{deci}f}.'.format(t=time, deci=P.DECI))

    def process(self):
        """ processes the end of service event """

        # trace
        self.urgentCare.trace.add_message('Processing end of exam in ' + str(self.examRoom) + '.')

        # process the end of service for this exam room
        self.urgentCare.process_end_of_exam(self.examRoom)


class CloseUrgentCare(SimLib.SimulationEvent):
    def __init__(self, time, urgent_care):
        """
        create the event to close the urgent care
        :param time: time of closure
        :param urgent_care: the urgent care
        """

        self.urgentCare = urgent_care

        # call the master class initialization
        SimLib.SimulationEvent.__init__(self, time, Priority.CLOSE.value)

        # trace
        urgent_care.trace.add_message(
            'Urgent care will close at time {t:.{deci}f}.'.format(t=time, deci=P.DECI))

    def process(self):
        """ processes the closing event
        :param urgent_care: the urgent care
        """
        # trace
        self.urgentCare.trace.add_message('Processing the closing event.')
        # close the urgent care
        self.urgentCare.ifOpen = False
