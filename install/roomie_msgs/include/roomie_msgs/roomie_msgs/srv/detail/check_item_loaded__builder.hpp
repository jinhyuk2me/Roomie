// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:srv/CheckItemLoaded.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/check_item_loaded.hpp"


#ifndef ROOMIE_MSGS__SRV__DETAIL__CHECK_ITEM_LOADED__BUILDER_HPP_
#define ROOMIE_MSGS__SRV__DETAIL__CHECK_ITEM_LOADED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/srv/detail/check_item_loaded__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_CheckItemLoaded_Request_robot_id
{
public:
  Init_CheckItemLoaded_Request_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::roomie_msgs::srv::CheckItemLoaded_Request robot_id(::roomie_msgs::srv::CheckItemLoaded_Request::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::CheckItemLoaded_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::CheckItemLoaded_Request>()
{
  return roomie_msgs::srv::builder::Init_CheckItemLoaded_Request_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_CheckItemLoaded_Response_item_loaded
{
public:
  explicit Init_CheckItemLoaded_Response_item_loaded(::roomie_msgs::srv::CheckItemLoaded_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::CheckItemLoaded_Response item_loaded(::roomie_msgs::srv::CheckItemLoaded_Response::_item_loaded_type arg)
  {
    msg_.item_loaded = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::CheckItemLoaded_Response msg_;
};

class Init_CheckItemLoaded_Response_robot_id
{
public:
  Init_CheckItemLoaded_Response_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CheckItemLoaded_Response_item_loaded robot_id(::roomie_msgs::srv::CheckItemLoaded_Response::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_CheckItemLoaded_Response_item_loaded(msg_);
  }

private:
  ::roomie_msgs::srv::CheckItemLoaded_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::CheckItemLoaded_Response>()
{
  return roomie_msgs::srv::builder::Init_CheckItemLoaded_Response_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_CheckItemLoaded_Event_response
{
public:
  explicit Init_CheckItemLoaded_Event_response(::roomie_msgs::srv::CheckItemLoaded_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::CheckItemLoaded_Event response(::roomie_msgs::srv::CheckItemLoaded_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::CheckItemLoaded_Event msg_;
};

class Init_CheckItemLoaded_Event_request
{
public:
  explicit Init_CheckItemLoaded_Event_request(::roomie_msgs::srv::CheckItemLoaded_Event & msg)
  : msg_(msg)
  {}
  Init_CheckItemLoaded_Event_response request(::roomie_msgs::srv::CheckItemLoaded_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_CheckItemLoaded_Event_response(msg_);
  }

private:
  ::roomie_msgs::srv::CheckItemLoaded_Event msg_;
};

class Init_CheckItemLoaded_Event_info
{
public:
  Init_CheckItemLoaded_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CheckItemLoaded_Event_request info(::roomie_msgs::srv::CheckItemLoaded_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_CheckItemLoaded_Event_request(msg_);
  }

private:
  ::roomie_msgs::srv::CheckItemLoaded_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::CheckItemLoaded_Event>()
{
  return roomie_msgs::srv::builder::Init_CheckItemLoaded_Event_info();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__SRV__DETAIL__CHECK_ITEM_LOADED__BUILDER_HPP_
