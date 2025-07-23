// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:msg/Arrival.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/arrival.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__ARRIVAL__BUILDER_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__ARRIVAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/msg/detail/arrival__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace msg
{

namespace builder
{

class Init_Arrival_location_id
{
public:
  explicit Init_Arrival_location_id(::roomie_msgs::msg::Arrival & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::msg::Arrival location_id(::roomie_msgs::msg::Arrival::_location_id_type arg)
  {
    msg_.location_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::msg::Arrival msg_;
};

class Init_Arrival_task_id
{
public:
  explicit Init_Arrival_task_id(::roomie_msgs::msg::Arrival & msg)
  : msg_(msg)
  {}
  Init_Arrival_location_id task_id(::roomie_msgs::msg::Arrival::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return Init_Arrival_location_id(msg_);
  }

private:
  ::roomie_msgs::msg::Arrival msg_;
};

class Init_Arrival_robot_id
{
public:
  Init_Arrival_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Arrival_task_id robot_id(::roomie_msgs::msg::Arrival::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_Arrival_task_id(msg_);
  }

private:
  ::roomie_msgs::msg::Arrival msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::msg::Arrival>()
{
  return roomie_msgs::msg::builder::Init_Arrival_robot_id();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__ARRIVAL__BUILDER_HPP_
