// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:msg/DeliveryCompleted.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/delivery_completed.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__DELIVERY_COMPLETED__BUILDER_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__DELIVERY_COMPLETED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/msg/detail/delivery_completed__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace msg
{

namespace builder
{

class Init_DeliveryCompleted_timestamp
{
public:
  explicit Init_DeliveryCompleted_timestamp(::roomie_msgs::msg::DeliveryCompleted & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::msg::DeliveryCompleted timestamp(::roomie_msgs::msg::DeliveryCompleted::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::msg::DeliveryCompleted msg_;
};

class Init_DeliveryCompleted_task_id
{
public:
  explicit Init_DeliveryCompleted_task_id(::roomie_msgs::msg::DeliveryCompleted & msg)
  : msg_(msg)
  {}
  Init_DeliveryCompleted_timestamp task_id(::roomie_msgs::msg::DeliveryCompleted::_task_id_type arg)
  {
    msg_.task_id = std::move(arg);
    return Init_DeliveryCompleted_timestamp(msg_);
  }

private:
  ::roomie_msgs::msg::DeliveryCompleted msg_;
};

class Init_DeliveryCompleted_robot_id
{
public:
  Init_DeliveryCompleted_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DeliveryCompleted_task_id robot_id(::roomie_msgs::msg::DeliveryCompleted::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_DeliveryCompleted_task_id(msg_);
  }

private:
  ::roomie_msgs::msg::DeliveryCompleted msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::msg::DeliveryCompleted>()
{
  return roomie_msgs::msg::builder::Init_DeliveryCompleted_robot_id();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__DELIVERY_COMPLETED__BUILDER_HPP_
