// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:msg/RobotState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/robot_state.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__ROBOT_STATE__BUILDER_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__ROBOT_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/msg/detail/robot_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace msg
{

namespace builder
{

class Init_RobotState_robot_state_id
{
public:
  explicit Init_RobotState_robot_state_id(::roomie_msgs::msg::RobotState & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::msg::RobotState robot_state_id(::roomie_msgs::msg::RobotState::_robot_state_id_type arg)
  {
    msg_.robot_state_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::msg::RobotState msg_;
};

class Init_RobotState_task_id
{
public:
  explicit Init_RobotState_task_id(::roomie_msgs::msg::RobotState & msg)
  : msg_(msg)
  {}
  Init_RobotState_robot_state_id task_id(::roomie_msgs::msg::RobotState::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return Init_RobotState_robot_state_id(msg_);
  }

private:
  ::roomie_msgs::msg::RobotState msg_;
};

class Init_RobotState_robot_id
{
public:
  Init_RobotState_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotState_task_id robot_id(::roomie_msgs::msg::RobotState::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_RobotState_task_id(msg_);
  }

private:
  ::roomie_msgs::msg::RobotState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::msg::RobotState>()
{
  return roomie_msgs::msg::builder::Init_RobotState_robot_id();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__ROBOT_STATE__BUILDER_HPP_
