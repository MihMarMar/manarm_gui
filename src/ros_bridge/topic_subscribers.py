import rospy

from src.ros_bridge.axes_subscriber import AxesSubscriber
from src.ros_bridge.image_subscriber import ImageSubscriber


# singleton for all subscribers
# noinspection PyClassHasNoInit
class TopicSubscribers:
    instance = None

    class __TopicSubscribers:

        def __init__(self):
            rospy.init_node("manarm_gui")
            self.axes_subscriber = AxesSubscriber()
            self.image_subscriber = ImageSubscriber()

    def __new__(cls, *args, **kwargs):
        if not TopicSubscribers.instance:
            TopicSubscribers.instance = TopicSubscribers.__TopicSubscribers()
        return TopicSubscribers.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, key, value):
        pass
