// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:msg/TrackingEvent.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/tracking_event.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__TRACKING_EVENT__BUILDER_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__TRACKING_EVENT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/msg/detail/tracking_event__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace msg
{

namespace builder
{

class Init_TrackingEvent_timestamp
{
public:
  explicit Init_TrackingEvent_timestamp(::roomie_msgs::msg::TrackingEvent & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::msg::TrackingEvent timestamp(::roomie_msgs::msg::TrackingEvent::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::msg::TrackingEvent msg_;
};

class Init_TrackingEvent_task_id
{
public:
  explicit Init_TrackingEvent_task_id(::roomie_msgs::msg::TrackingEvent & msg)
  : msg_(msg)
  {}
  Init_TrackingEvent_timestamp task_id(::roomie_msgs::msg::TrackingEvent::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return Init_TrackingEvent_timestamp(msg_);
  }

private:
  ::roomie_msgs::msg::TrackingEvent msg_;
};

class Init_TrackingEvent_tracking_event_id
{
public:
  explicit Init_TrackingEvent_tracking_event_id(::roomie_msgs::msg::TrackingEvent & msg)
  : msg_(msg)
  {}
  Init_TrackingEvent_task_id tracking_event_id(::roomie_msgs::msg::TrackingEvent::_tracking_event_id_type arg)
  {
    msg_.tracking_event_id = std::move(arg);
    return Init_TrackingEvent_task_id(msg_);
  }

private:
  ::roomie_msgs::msg::TrackingEvent msg_;
};

class Init_TrackingEvent_robot_id
{
public:
  Init_TrackingEvent_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TrackingEvent_tracking_event_id robot_id(::roomie_msgs::msg::TrackingEvent::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_TrackingEvent_tracking_event_id(msg_);
  }

private:
  ::roomie_msgs::msg::TrackingEvent msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::msg::TrackingEvent>()
{
  return roomie_msgs::msg::builder::Init_TrackingEvent_robot_id();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__TRACKING_EVENT__BUILDER_HPP_
