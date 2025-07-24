// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:srv/ButtonStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/button_status.hpp"


#ifndef ROOMIE_MSGS__SRV__DETAIL__BUTTON_STATUS__BUILDER_HPP_
#define ROOMIE_MSGS__SRV__DETAIL__BUTTON_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/srv/detail/button_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_ButtonStatus_Request_button_ids
{
public:
  explicit Init_ButtonStatus_Request_button_ids(::roomie_msgs::srv::ButtonStatus_Request & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::ButtonStatus_Request button_ids(::roomie_msgs::srv::ButtonStatus_Request::_button_ids_type arg)
  {
    msg_.button_ids = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::ButtonStatus_Request msg_;
};

class Init_ButtonStatus_Request_robot_id
{
public:
  Init_ButtonStatus_Request_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ButtonStatus_Request_button_ids robot_id(::roomie_msgs::srv::ButtonStatus_Request::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_ButtonStatus_Request_button_ids(msg_);
  }

private:
  ::roomie_msgs::srv::ButtonStatus_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::ButtonStatus_Request>()
{
  return roomie_msgs::srv::builder::Init_ButtonStatus_Request_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_ButtonStatus_Response_timestamp
{
public:
  explicit Init_ButtonStatus_Response_timestamp(::roomie_msgs::srv::ButtonStatus_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::ButtonStatus_Response timestamp(::roomie_msgs::srv::ButtonStatus_Response::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::ButtonStatus_Response msg_;
};

class Init_ButtonStatus_Response_is_pressed
{
public:
  explicit Init_ButtonStatus_Response_is_pressed(::roomie_msgs::srv::ButtonStatus_Response & msg)
  : msg_(msg)
  {}
  Init_ButtonStatus_Response_timestamp is_pressed(::roomie_msgs::srv::ButtonStatus_Response::_is_pressed_type arg)
  {
    msg_.is_pressed = std::move(arg);
    return Init_ButtonStatus_Response_timestamp(msg_);
  }

private:
  ::roomie_msgs::srv::ButtonStatus_Response msg_;
};

class Init_ButtonStatus_Response_depths
{
public:
  explicit Init_ButtonStatus_Response_depths(::roomie_msgs::srv::ButtonStatus_Response & msg)
  : msg_(msg)
  {}
  Init_ButtonStatus_Response_is_pressed depths(::roomie_msgs::srv::ButtonStatus_Response::_depths_type arg)
  {
    msg_.depths = std::move(arg);
    return Init_ButtonStatus_Response_is_pressed(msg_);
  }

private:
  ::roomie_msgs::srv::ButtonStatus_Response msg_;
};

class Init_ButtonStatus_Response_ys
{
public:
  explicit Init_ButtonStatus_Response_ys(::roomie_msgs::srv::ButtonStatus_Response & msg)
  : msg_(msg)
  {}
  Init_ButtonStatus_Response_depths ys(::roomie_msgs::srv::ButtonStatus_Response::_ys_type arg)
  {
    msg_.ys = std::move(arg);
    return Init_ButtonStatus_Response_depths(msg_);
  }

private:
  ::roomie_msgs::srv::ButtonStatus_Response msg_;
};

class Init_ButtonStatus_Response_xs
{
public:
  explicit Init_ButtonStatus_Response_xs(::roomie_msgs::srv::ButtonStatus_Response & msg)
  : msg_(msg)
  {}
  Init_ButtonStatus_Response_ys xs(::roomie_msgs::srv::ButtonStatus_Response::_xs_type arg)
  {
    msg_.xs = std::move(arg);
    return Init_ButtonStatus_Response_ys(msg_);
  }

private:
  ::roomie_msgs::srv::ButtonStatus_Response msg_;
};

class Init_ButtonStatus_Response_robot_id
{
public:
  Init_ButtonStatus_Response_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ButtonStatus_Response_xs robot_id(::roomie_msgs::srv::ButtonStatus_Response::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_ButtonStatus_Response_xs(msg_);
  }

private:
  ::roomie_msgs::srv::ButtonStatus_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::ButtonStatus_Response>()
{
  return roomie_msgs::srv::builder::Init_ButtonStatus_Response_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_ButtonStatus_Event_response
{
public:
  explicit Init_ButtonStatus_Event_response(::roomie_msgs::srv::ButtonStatus_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::ButtonStatus_Event response(::roomie_msgs::srv::ButtonStatus_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::ButtonStatus_Event msg_;
};

class Init_ButtonStatus_Event_request
{
public:
  explicit Init_ButtonStatus_Event_request(::roomie_msgs::srv::ButtonStatus_Event & msg)
  : msg_(msg)
  {}
  Init_ButtonStatus_Event_response request(::roomie_msgs::srv::ButtonStatus_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_ButtonStatus_Event_response(msg_);
  }

private:
  ::roomie_msgs::srv::ButtonStatus_Event msg_;
};

class Init_ButtonStatus_Event_info
{
public:
  Init_ButtonStatus_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ButtonStatus_Event_request info(::roomie_msgs::srv::ButtonStatus_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_ButtonStatus_Event_request(msg_);
  }

private:
  ::roomie_msgs::srv::ButtonStatus_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::ButtonStatus_Event>()
{
  return roomie_msgs::srv::builder::Init_ButtonStatus_Event_info();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__SRV__DETAIL__BUTTON_STATUS__BUILDER_HPP_
