// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:msg/PickupCompleted.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/pickup_completed.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__PICKUP_COMPLETED__BUILDER_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__PICKUP_COMPLETED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/msg/detail/pickup_completed__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace msg
{

namespace builder
{

class Init_PickupCompleted_timestamp
{
public:
  explicit Init_PickupCompleted_timestamp(::roomie_msgs::msg::PickupCompleted & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::msg::PickupCompleted timestamp(::roomie_msgs::msg::PickupCompleted::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::msg::PickupCompleted msg_;
};

class Init_PickupCompleted_task_id
{
public:
  explicit Init_PickupCompleted_task_id(::roomie_msgs::msg::PickupCompleted & msg)
  : msg_(msg)
  {}
  Init_PickupCompleted_timestamp task_id(::roomie_msgs::msg::PickupCompleted::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return Init_PickupCompleted_timestamp(msg_);
  }

private:
  ::roomie_msgs::msg::PickupCompleted msg_;
};

class Init_PickupCompleted_robot_id
{
public:
  Init_PickupCompleted_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PickupCompleted_task_id robot_id(::roomie_msgs::msg::PickupCompleted::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_PickupCompleted_task_id(msg_);
  }

private:
  ::roomie_msgs::msg::PickupCompleted msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::msg::PickupCompleted>()
{
  return roomie_msgs::msg::builder::Init_PickupCompleted_robot_id();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__PICKUP_COMPLETED__BUILDER_HPP_
