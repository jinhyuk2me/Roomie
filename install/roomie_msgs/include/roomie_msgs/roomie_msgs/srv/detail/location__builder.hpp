// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:srv/Location.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/location.hpp"


#ifndef ROOMIE_MSGS__SRV__DETAIL__LOCATION__BUILDER_HPP_
#define ROOMIE_MSGS__SRV__DETAIL__LOCATION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/srv/detail/location__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_Location_Request_robot_id
{
public:
  Init_Location_Request_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::roomie_msgs::srv::Location_Request robot_id(::roomie_msgs::srv::Location_Request::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::Location_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::Location_Request>()
{
  return roomie_msgs::srv::builder::Init_Location_Request_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_Location_Response_location_id
{
public:
  explicit Init_Location_Response_location_id(::roomie_msgs::srv::Location_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::Location_Response location_id(::roomie_msgs::srv::Location_Response::_location_id_type arg)
  {
    msg_.location_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::Location_Response msg_;
};

class Init_Location_Response_success
{
public:
  explicit Init_Location_Response_success(::roomie_msgs::srv::Location_Response & msg)
  : msg_(msg)
  {}
  Init_Location_Response_location_id success(::roomie_msgs::srv::Location_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_Location_Response_location_id(msg_);
  }

private:
  ::roomie_msgs::srv::Location_Response msg_;
};

class Init_Location_Response_robot_id
{
public:
  Init_Location_Response_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Location_Response_success robot_id(::roomie_msgs::srv::Location_Response::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_Location_Response_success(msg_);
  }

private:
  ::roomie_msgs::srv::Location_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::Location_Response>()
{
  return roomie_msgs::srv::builder::Init_Location_Response_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_Location_Event_response
{
public:
  explicit Init_Location_Event_response(::roomie_msgs::srv::Location_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::Location_Event response(::roomie_msgs::srv::Location_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::Location_Event msg_;
};

class Init_Location_Event_request
{
public:
  explicit Init_Location_Event_request(::roomie_msgs::srv::Location_Event & msg)
  : msg_(msg)
  {}
  Init_Location_Event_response request(::roomie_msgs::srv::Location_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_Location_Event_response(msg_);
  }

private:
  ::roomie_msgs::srv::Location_Event msg_;
};

class Init_Location_Event_info
{
public:
  Init_Location_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Location_Event_request info(::roomie_msgs::srv::Location_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_Location_Event_request(msg_);
  }

private:
  ::roomie_msgs::srv::Location_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::Location_Event>()
{
  return roomie_msgs::srv::builder::Init_Location_Event_info();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__SRV__DETAIL__LOCATION__BUILDER_HPP_
