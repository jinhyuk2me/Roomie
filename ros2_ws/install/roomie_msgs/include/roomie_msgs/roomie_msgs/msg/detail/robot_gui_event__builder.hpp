// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:msg/RobotGuiEvent.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/robot_gui_event.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__ROBOT_GUI_EVENT__BUILDER_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__ROBOT_GUI_EVENT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/msg/detail/robot_gui_event__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace msg
{

namespace builder
{

class Init_RobotGuiEvent_detail
{
public:
  explicit Init_RobotGuiEvent_detail(::roomie_msgs::msg::RobotGuiEvent & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::msg::RobotGuiEvent detail(::roomie_msgs::msg::RobotGuiEvent::_detail_type arg)
  {
    msg_.detail = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::msg::RobotGuiEvent msg_;
};

class Init_RobotGuiEvent_timestamp
{
public:
  explicit Init_RobotGuiEvent_timestamp(::roomie_msgs::msg::RobotGuiEvent & msg)
  : msg_(msg)
  {}
  Init_RobotGuiEvent_detail timestamp(::roomie_msgs::msg::RobotGuiEvent::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_RobotGuiEvent_detail(msg_);
  }

private:
  ::roomie_msgs::msg::RobotGuiEvent msg_;
};

class Init_RobotGuiEvent_task_id
{
public:
  explicit Init_RobotGuiEvent_task_id(::roomie_msgs::msg::RobotGuiEvent & msg)
  : msg_(msg)
  {}
  Init_RobotGuiEvent_timestamp task_id(::roomie_msgs::msg::RobotGuiEvent::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return Init_RobotGuiEvent_timestamp(msg_);
  }

private:
  ::roomie_msgs::msg::RobotGuiEvent msg_;
};

class Init_RobotGuiEvent_rgui_event_id
{
public:
  explicit Init_RobotGuiEvent_rgui_event_id(::roomie_msgs::msg::RobotGuiEvent & msg)
  : msg_(msg)
  {}
  Init_RobotGuiEvent_task_id rgui_event_id(::roomie_msgs::msg::RobotGuiEvent::_rgui_event_id_type arg)
  {
    msg_.rgui_event_id = std::move(arg);
    return Init_RobotGuiEvent_task_id(msg_);
  }

private:
  ::roomie_msgs::msg::RobotGuiEvent msg_;
};

class Init_RobotGuiEvent_robot_id
{
public:
  Init_RobotGuiEvent_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotGuiEvent_rgui_event_id robot_id(::roomie_msgs::msg::RobotGuiEvent::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_RobotGuiEvent_rgui_event_id(msg_);
  }

private:
  ::roomie_msgs::msg::RobotGuiEvent msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::msg::RobotGuiEvent>()
{
  return roomie_msgs::msg::builder::Init_RobotGuiEvent_robot_id();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__ROBOT_GUI_EVENT__BUILDER_HPP_
