// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:srv/ControlLock.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/control_lock.hpp"


#ifndef ROOMIE_MSGS__SRV__DETAIL__CONTROL_LOCK__BUILDER_HPP_
#define ROOMIE_MSGS__SRV__DETAIL__CONTROL_LOCK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/srv/detail/control_lock__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_ControlLock_Request_locked
{
public:
  explicit Init_ControlLock_Request_locked(::roomie_msgs::srv::ControlLock_Request & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::ControlLock_Request locked(::roomie_msgs::srv::ControlLock_Request::_locked_type arg)
  {
    msg_.locked = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::ControlLock_Request msg_;
};

class Init_ControlLock_Request_robot_id
{
public:
  Init_ControlLock_Request_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlLock_Request_locked robot_id(::roomie_msgs::srv::ControlLock_Request::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_ControlLock_Request_locked(msg_);
  }

private:
  ::roomie_msgs::srv::ControlLock_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::ControlLock_Request>()
{
  return roomie_msgs::srv::builder::Init_ControlLock_Request_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_ControlLock_Response_success
{
public:
  explicit Init_ControlLock_Response_success(::roomie_msgs::srv::ControlLock_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::ControlLock_Response success(::roomie_msgs::srv::ControlLock_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::ControlLock_Response msg_;
};

class Init_ControlLock_Response_robot_id
{
public:
  Init_ControlLock_Response_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlLock_Response_success robot_id(::roomie_msgs::srv::ControlLock_Response::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_ControlLock_Response_success(msg_);
  }

private:
  ::roomie_msgs::srv::ControlLock_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::ControlLock_Response>()
{
  return roomie_msgs::srv::builder::Init_ControlLock_Response_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_ControlLock_Event_response
{
public:
  explicit Init_ControlLock_Event_response(::roomie_msgs::srv::ControlLock_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::ControlLock_Event response(::roomie_msgs::srv::ControlLock_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::ControlLock_Event msg_;
};

class Init_ControlLock_Event_request
{
public:
  explicit Init_ControlLock_Event_request(::roomie_msgs::srv::ControlLock_Event & msg)
  : msg_(msg)
  {}
  Init_ControlLock_Event_response request(::roomie_msgs::srv::ControlLock_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_ControlLock_Event_response(msg_);
  }

private:
  ::roomie_msgs::srv::ControlLock_Event msg_;
};

class Init_ControlLock_Event_info
{
public:
  Init_ControlLock_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlLock_Event_request info(::roomie_msgs::srv::ControlLock_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_ControlLock_Event_request(msg_);
  }

private:
  ::roomie_msgs::srv::ControlLock_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::ControlLock_Event>()
{
  return roomie_msgs::srv::builder::Init_ControlLock_Event_info();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__SRV__DETAIL__CONTROL_LOCK__BUILDER_HPP_
