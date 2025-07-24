// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:msg/Registered.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/registered.hpp"


#ifndef ROOMIE_MSGS__MSG__DETAIL__REGISTERED__BUILDER_HPP_
#define ROOMIE_MSGS__MSG__DETAIL__REGISTERED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/msg/detail/registered__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace msg
{

namespace builder
{

class Init_Registered_timestamp
{
public:
  explicit Init_Registered_timestamp(::roomie_msgs::msg::Registered & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::msg::Registered timestamp(::roomie_msgs::msg::Registered::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::msg::Registered msg_;
};

class Init_Registered_robot_id
{
public:
  Init_Registered_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Registered_timestamp robot_id(::roomie_msgs::msg::Registered::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_Registered_timestamp(msg_);
  }

private:
  ::roomie_msgs::msg::Registered msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::msg::Registered>()
{
  return roomie_msgs::msg::builder::Init_Registered_robot_id();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__MSG__DETAIL__REGISTERED__BUILDER_HPP_
