// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from roomie_msgs:srv/GetLocations.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/get_locations.hpp"


#ifndef ROOMIE_MSGS__SRV__DETAIL__GET_LOCATIONS__BUILDER_HPP_
#define ROOMIE_MSGS__SRV__DETAIL__GET_LOCATIONS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "roomie_msgs/srv/detail/get_locations__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_GetLocations_Request_robot_id
{
public:
  Init_GetLocations_Request_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::roomie_msgs::srv::GetLocations_Request robot_id(::roomie_msgs::srv::GetLocations_Request::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::GetLocations_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::GetLocations_Request>()
{
  return roomie_msgs::srv::builder::Init_GetLocations_Request_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_GetLocations_Response_location_ys
{
public:
  explicit Init_GetLocations_Response_location_ys(::roomie_msgs::srv::GetLocations_Response & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::GetLocations_Response location_ys(::roomie_msgs::srv::GetLocations_Response::_location_ys_type arg)
  {
    msg_.location_ys = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::GetLocations_Response msg_;
};

class Init_GetLocations_Response_location_xs
{
public:
  explicit Init_GetLocations_Response_location_xs(::roomie_msgs::srv::GetLocations_Response & msg)
  : msg_(msg)
  {}
  Init_GetLocations_Response_location_ys location_xs(::roomie_msgs::srv::GetLocations_Response::_location_xs_type arg)
  {
    msg_.location_xs = std::move(arg);
    return Init_GetLocations_Response_location_ys(msg_);
  }

private:
  ::roomie_msgs::srv::GetLocations_Response msg_;
};

class Init_GetLocations_Response_floor_ids
{
public:
  explicit Init_GetLocations_Response_floor_ids(::roomie_msgs::srv::GetLocations_Response & msg)
  : msg_(msg)
  {}
  Init_GetLocations_Response_location_xs floor_ids(::roomie_msgs::srv::GetLocations_Response::_floor_ids_type arg)
  {
    msg_.floor_ids = std::move(arg);
    return Init_GetLocations_Response_location_xs(msg_);
  }

private:
  ::roomie_msgs::srv::GetLocations_Response msg_;
};

class Init_GetLocations_Response_location_ids
{
public:
  explicit Init_GetLocations_Response_location_ids(::roomie_msgs::srv::GetLocations_Response & msg)
  : msg_(msg)
  {}
  Init_GetLocations_Response_floor_ids location_ids(::roomie_msgs::srv::GetLocations_Response::_location_ids_type arg)
  {
    msg_.location_ids = std::move(arg);
    return Init_GetLocations_Response_floor_ids(msg_);
  }

private:
  ::roomie_msgs::srv::GetLocations_Response msg_;
};

class Init_GetLocations_Response_success
{
public:
  explicit Init_GetLocations_Response_success(::roomie_msgs::srv::GetLocations_Response & msg)
  : msg_(msg)
  {}
  Init_GetLocations_Response_location_ids success(::roomie_msgs::srv::GetLocations_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_GetLocations_Response_location_ids(msg_);
  }

private:
  ::roomie_msgs::srv::GetLocations_Response msg_;
};

class Init_GetLocations_Response_robot_id
{
public:
  Init_GetLocations_Response_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetLocations_Response_success robot_id(::roomie_msgs::srv::GetLocations_Response::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_GetLocations_Response_success(msg_);
  }

private:
  ::roomie_msgs::srv::GetLocations_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::GetLocations_Response>()
{
  return roomie_msgs::srv::builder::Init_GetLocations_Response_robot_id();
}

}  // namespace roomie_msgs


namespace roomie_msgs
{

namespace srv
{

namespace builder
{

class Init_GetLocations_Event_response
{
public:
  explicit Init_GetLocations_Event_response(::roomie_msgs::srv::GetLocations_Event & msg)
  : msg_(msg)
  {}
  ::roomie_msgs::srv::GetLocations_Event response(::roomie_msgs::srv::GetLocations_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::roomie_msgs::srv::GetLocations_Event msg_;
};

class Init_GetLocations_Event_request
{
public:
  explicit Init_GetLocations_Event_request(::roomie_msgs::srv::GetLocations_Event & msg)
  : msg_(msg)
  {}
  Init_GetLocations_Event_response request(::roomie_msgs::srv::GetLocations_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_GetLocations_Event_response(msg_);
  }

private:
  ::roomie_msgs::srv::GetLocations_Event msg_;
};

class Init_GetLocations_Event_info
{
public:
  Init_GetLocations_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetLocations_Event_request info(::roomie_msgs::srv::GetLocations_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_GetLocations_Event_request(msg_);
  }

private:
  ::roomie_msgs::srv::GetLocations_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::roomie_msgs::srv::GetLocations_Event>()
{
  return roomie_msgs::srv::builder::Init_GetLocations_Event_info();
}

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__SRV__DETAIL__GET_LOCATIONS__BUILDER_HPP_
