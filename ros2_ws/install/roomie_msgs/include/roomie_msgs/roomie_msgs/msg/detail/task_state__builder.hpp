// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:msg/TaskState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/task_state.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__TASK_STATE__BUILDER_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__TASK_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/msg/detail/task_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace msg
{

namespace builder
{

class Init_TaskState_task_state_id
{
public:
  explicit Init_TaskState_task_state_id(::roomie_msgs::msg::TaskState & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::msg::TaskState task_state_id(::roomie_msgs::msg::TaskState::_task_state_id_type arg)
  {
    msg_.task_state_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::msg::TaskState msg_;
};

class Init_TaskState_task_id
{
public:
  Init_TaskState_task_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskState_task_state_id task_id(::roomie_msgs::msg::TaskState::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return Init_TaskState_task_state_id(msg_);
  }

private:
  ::roomie_msgs::msg::TaskState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::msg::TaskState>()
{
  return roomie_msgs::msg::builder::Init_TaskState_task_id();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__TASK_STATE__BUILDER_HPP_
