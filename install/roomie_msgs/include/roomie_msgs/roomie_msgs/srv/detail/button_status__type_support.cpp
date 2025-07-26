// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from roomie_msgs:srv/ButtonStatus.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "roomie_msgs/srv/detail/button_status__functions.h"
#include "roomie_msgs/srv/detail/button_status__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace roomie_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void ButtonStatus_Request_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) roomie_msgs::srv::ButtonStatus_Request(_init);
}

void ButtonStatus_Request_fini_function(void * message_memory)
{
  auto typed_message = static_cast<roomie_msgs::srv::ButtonStatus_Request *>(message_memory);
  typed_message->~ButtonStatus_Request();
}

size_t size_function__ButtonStatus_Request__button_ids(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ButtonStatus_Request__button_ids(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__ButtonStatus_Request__button_ids(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__ButtonStatus_Request__button_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__ButtonStatus_Request__button_ids(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__ButtonStatus_Request__button_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__ButtonStatus_Request__button_ids(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__ButtonStatus_Request__button_ids(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember ButtonStatus_Request_message_member_array[2] = {
  {
    "robot_id",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs::srv::ButtonStatus_Request, robot_id),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "button_ids",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs::srv::ButtonStatus_Request, button_ids),  // bytes offset in struct
    nullptr,  // default value
    size_function__ButtonStatus_Request__button_ids,  // size() function pointer
    get_const_function__ButtonStatus_Request__button_ids,  // get_const(index) function pointer
    get_function__ButtonStatus_Request__button_ids,  // get(index) function pointer
    fetch_function__ButtonStatus_Request__button_ids,  // fetch(index, &value) function pointer
    assign_function__ButtonStatus_Request__button_ids,  // assign(index, value) function pointer
    resize_function__ButtonStatus_Request__button_ids  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers ButtonStatus_Request_message_members = {
  "roomie_msgs::srv",  // message namespace
  "ButtonStatus_Request",  // message name
  2,  // number of fields
  sizeof(roomie_msgs::srv::ButtonStatus_Request),
  false,  // has_any_key_member_
  ButtonStatus_Request_message_member_array,  // message members
  ButtonStatus_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  ButtonStatus_Request_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t ButtonStatus_Request_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ButtonStatus_Request_message_members,
  get_message_typesupport_handle_function,
  &roomie_msgs__srv__ButtonStatus_Request__get_type_hash,
  &roomie_msgs__srv__ButtonStatus_Request__get_type_description,
  &roomie_msgs__srv__ButtonStatus_Request__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace roomie_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<roomie_msgs::srv::ButtonStatus_Request>()
{
  return &::roomie_msgs::srv::rosidl_typesupport_introspection_cpp::ButtonStatus_Request_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, roomie_msgs, srv, ButtonStatus_Request)() {
  return &::roomie_msgs::srv::rosidl_typesupport_introspection_cpp::ButtonStatus_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "array"
// already included above
// #include "cstddef"
// already included above
// #include "string"
// already included above
// #include "vector"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "roomie_msgs/srv/detail/button_status__functions.h"
// already included above
// #include "roomie_msgs/srv/detail/button_status__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/field_types.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace roomie_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void ButtonStatus_Response_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) roomie_msgs::srv::ButtonStatus_Response(_init);
}

void ButtonStatus_Response_fini_function(void * message_memory)
{
  auto typed_message = static_cast<roomie_msgs::srv::ButtonStatus_Response *>(message_memory);
  typed_message->~ButtonStatus_Response();
}

size_t size_function__ButtonStatus_Response__xs(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ButtonStatus_Response__xs(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__ButtonStatus_Response__xs(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__ButtonStatus_Response__xs(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__ButtonStatus_Response__xs(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__ButtonStatus_Response__xs(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__ButtonStatus_Response__xs(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__ButtonStatus_Response__xs(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__ButtonStatus_Response__ys(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ButtonStatus_Response__ys(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__ButtonStatus_Response__ys(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__ButtonStatus_Response__ys(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__ButtonStatus_Response__ys(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__ButtonStatus_Response__ys(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__ButtonStatus_Response__ys(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__ButtonStatus_Response__ys(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__ButtonStatus_Response__depths(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ButtonStatus_Response__depths(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__ButtonStatus_Response__depths(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__ButtonStatus_Response__depths(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__ButtonStatus_Response__depths(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__ButtonStatus_Response__depths(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__ButtonStatus_Response__depths(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__ButtonStatus_Response__depths(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__ButtonStatus_Response__is_pressed(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<bool> *>(untyped_member);
  return member->size();
}

void fetch_function__ButtonStatus_Response__is_pressed(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & member = *reinterpret_cast<const std::vector<bool> *>(untyped_member);
  auto & value = *reinterpret_cast<bool *>(untyped_value);
  value = member[index];
}

void assign_function__ButtonStatus_Response__is_pressed(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & member = *reinterpret_cast<std::vector<bool> *>(untyped_member);
  const auto & value = *reinterpret_cast<const bool *>(untyped_value);
  member[index] = value;
}

void resize_function__ButtonStatus_Response__is_pressed(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<bool> *>(untyped_member);
  member->resize(size);
}

size_t size_function__ButtonStatus_Response__timestamp(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<builtin_interfaces::msg::Time> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ButtonStatus_Response__timestamp(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<builtin_interfaces::msg::Time> *>(untyped_member);
  return &member[index];
}

void * get_function__ButtonStatus_Response__timestamp(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<builtin_interfaces::msg::Time> *>(untyped_member);
  return &member[index];
}

void fetch_function__ButtonStatus_Response__timestamp(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const builtin_interfaces::msg::Time *>(
    get_const_function__ButtonStatus_Response__timestamp(untyped_member, index));
  auto & value = *reinterpret_cast<builtin_interfaces::msg::Time *>(untyped_value);
  value = item;
}

void assign_function__ButtonStatus_Response__timestamp(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<builtin_interfaces::msg::Time *>(
    get_function__ButtonStatus_Response__timestamp(untyped_member, index));
  const auto & value = *reinterpret_cast<const builtin_interfaces::msg::Time *>(untyped_value);
  item = value;
}

void resize_function__ButtonStatus_Response__timestamp(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<builtin_interfaces::msg::Time> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember ButtonStatus_Response_message_member_array[7] = {
  {
    "robot_id",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs::srv::ButtonStatus_Response, robot_id),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "success",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs::srv::ButtonStatus_Response, success),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "xs",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs::srv::ButtonStatus_Response, xs),  // bytes offset in struct
    nullptr,  // default value
    size_function__ButtonStatus_Response__xs,  // size() function pointer
    get_const_function__ButtonStatus_Response__xs,  // get_const(index) function pointer
    get_function__ButtonStatus_Response__xs,  // get(index) function pointer
    fetch_function__ButtonStatus_Response__xs,  // fetch(index, &value) function pointer
    assign_function__ButtonStatus_Response__xs,  // assign(index, value) function pointer
    resize_function__ButtonStatus_Response__xs  // resize(index) function pointer
  },
  {
    "ys",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs::srv::ButtonStatus_Response, ys),  // bytes offset in struct
    nullptr,  // default value
    size_function__ButtonStatus_Response__ys,  // size() function pointer
    get_const_function__ButtonStatus_Response__ys,  // get_const(index) function pointer
    get_function__ButtonStatus_Response__ys,  // get(index) function pointer
    fetch_function__ButtonStatus_Response__ys,  // fetch(index, &value) function pointer
    assign_function__ButtonStatus_Response__ys,  // assign(index, value) function pointer
    resize_function__ButtonStatus_Response__ys  // resize(index) function pointer
  },
  {
    "depths",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs::srv::ButtonStatus_Response, depths),  // bytes offset in struct
    nullptr,  // default value
    size_function__ButtonStatus_Response__depths,  // size() function pointer
    get_const_function__ButtonStatus_Response__depths,  // get_const(index) function pointer
    get_function__ButtonStatus_Response__depths,  // get(index) function pointer
    fetch_function__ButtonStatus_Response__depths,  // fetch(index, &value) function pointer
    assign_function__ButtonStatus_Response__depths,  // assign(index, value) function pointer
    resize_function__ButtonStatus_Response__depths  // resize(index) function pointer
  },
  {
    "is_pressed",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs::srv::ButtonStatus_Response, is_pressed),  // bytes offset in struct
    nullptr,  // default value
    size_function__ButtonStatus_Response__is_pressed,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    fetch_function__ButtonStatus_Response__is_pressed,  // fetch(index, &value) function pointer
    assign_function__ButtonStatus_Response__is_pressed,  // assign(index, value) function pointer
    resize_function__ButtonStatus_Response__is_pressed  // resize(index) function pointer
  },
  {
    "timestamp",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<builtin_interfaces::msg::Time>(),  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs::srv::ButtonStatus_Response, timestamp),  // bytes offset in struct
    nullptr,  // default value
    size_function__ButtonStatus_Response__timestamp,  // size() function pointer
    get_const_function__ButtonStatus_Response__timestamp,  // get_const(index) function pointer
    get_function__ButtonStatus_Response__timestamp,  // get(index) function pointer
    fetch_function__ButtonStatus_Response__timestamp,  // fetch(index, &value) function pointer
    assign_function__ButtonStatus_Response__timestamp,  // assign(index, value) function pointer
    resize_function__ButtonStatus_Response__timestamp  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers ButtonStatus_Response_message_members = {
  "roomie_msgs::srv",  // message namespace
  "ButtonStatus_Response",  // message name
  7,  // number of fields
  sizeof(roomie_msgs::srv::ButtonStatus_Response),
  false,  // has_any_key_member_
  ButtonStatus_Response_message_member_array,  // message members
  ButtonStatus_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  ButtonStatus_Response_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t ButtonStatus_Response_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ButtonStatus_Response_message_members,
  get_message_typesupport_handle_function,
  &roomie_msgs__srv__ButtonStatus_Response__get_type_hash,
  &roomie_msgs__srv__ButtonStatus_Response__get_type_description,
  &roomie_msgs__srv__ButtonStatus_Response__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace roomie_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<roomie_msgs::srv::ButtonStatus_Response>()
{
  return &::roomie_msgs::srv::rosidl_typesupport_introspection_cpp::ButtonStatus_Response_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, roomie_msgs, srv, ButtonStatus_Response)() {
  return &::roomie_msgs::srv::rosidl_typesupport_introspection_cpp::ButtonStatus_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "array"
// already included above
// #include "cstddef"
// already included above
// #include "string"
// already included above
// #include "vector"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "roomie_msgs/srv/detail/button_status__functions.h"
// already included above
// #include "roomie_msgs/srv/detail/button_status__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/field_types.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace roomie_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void ButtonStatus_Event_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) roomie_msgs::srv::ButtonStatus_Event(_init);
}

void ButtonStatus_Event_fini_function(void * message_memory)
{
  auto typed_message = static_cast<roomie_msgs::srv::ButtonStatus_Event *>(message_memory);
  typed_message->~ButtonStatus_Event();
}

size_t size_function__ButtonStatus_Event__request(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<roomie_msgs::srv::ButtonStatus_Request> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ButtonStatus_Event__request(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<roomie_msgs::srv::ButtonStatus_Request> *>(untyped_member);
  return &member[index];
}

void * get_function__ButtonStatus_Event__request(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<roomie_msgs::srv::ButtonStatus_Request> *>(untyped_member);
  return &member[index];
}

void fetch_function__ButtonStatus_Event__request(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const roomie_msgs::srv::ButtonStatus_Request *>(
    get_const_function__ButtonStatus_Event__request(untyped_member, index));
  auto & value = *reinterpret_cast<roomie_msgs::srv::ButtonStatus_Request *>(untyped_value);
  value = item;
}

void assign_function__ButtonStatus_Event__request(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<roomie_msgs::srv::ButtonStatus_Request *>(
    get_function__ButtonStatus_Event__request(untyped_member, index));
  const auto & value = *reinterpret_cast<const roomie_msgs::srv::ButtonStatus_Request *>(untyped_value);
  item = value;
}

void resize_function__ButtonStatus_Event__request(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<roomie_msgs::srv::ButtonStatus_Request> *>(untyped_member);
  member->resize(size);
}

size_t size_function__ButtonStatus_Event__response(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<roomie_msgs::srv::ButtonStatus_Response> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ButtonStatus_Event__response(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<roomie_msgs::srv::ButtonStatus_Response> *>(untyped_member);
  return &member[index];
}

void * get_function__ButtonStatus_Event__response(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<roomie_msgs::srv::ButtonStatus_Response> *>(untyped_member);
  return &member[index];
}

void fetch_function__ButtonStatus_Event__response(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const roomie_msgs::srv::ButtonStatus_Response *>(
    get_const_function__ButtonStatus_Event__response(untyped_member, index));
  auto & value = *reinterpret_cast<roomie_msgs::srv::ButtonStatus_Response *>(untyped_value);
  value = item;
}

void assign_function__ButtonStatus_Event__response(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<roomie_msgs::srv::ButtonStatus_Response *>(
    get_function__ButtonStatus_Event__response(untyped_member, index));
  const auto & value = *reinterpret_cast<const roomie_msgs::srv::ButtonStatus_Response *>(untyped_value);
  item = value;
}

void resize_function__ButtonStatus_Event__response(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<roomie_msgs::srv::ButtonStatus_Response> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember ButtonStatus_Event_message_member_array[3] = {
  {
    "info",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<service_msgs::msg::ServiceEventInfo>(),  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs::srv::ButtonStatus_Event, info),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "request",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<roomie_msgs::srv::ButtonStatus_Request>(),  // members of sub message
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(roomie_msgs::srv::ButtonStatus_Event, request),  // bytes offset in struct
    nullptr,  // default value
    size_function__ButtonStatus_Event__request,  // size() function pointer
    get_const_function__ButtonStatus_Event__request,  // get_const(index) function pointer
    get_function__ButtonStatus_Event__request,  // get(index) function pointer
    fetch_function__ButtonStatus_Event__request,  // fetch(index, &value) function pointer
    assign_function__ButtonStatus_Event__request,  // assign(index, value) function pointer
    resize_function__ButtonStatus_Event__request  // resize(index) function pointer
  },
  {
    "response",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<roomie_msgs::srv::ButtonStatus_Response>(),  // members of sub message
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(roomie_msgs::srv::ButtonStatus_Event, response),  // bytes offset in struct
    nullptr,  // default value
    size_function__ButtonStatus_Event__response,  // size() function pointer
    get_const_function__ButtonStatus_Event__response,  // get_const(index) function pointer
    get_function__ButtonStatus_Event__response,  // get(index) function pointer
    fetch_function__ButtonStatus_Event__response,  // fetch(index, &value) function pointer
    assign_function__ButtonStatus_Event__response,  // assign(index, value) function pointer
    resize_function__ButtonStatus_Event__response  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers ButtonStatus_Event_message_members = {
  "roomie_msgs::srv",  // message namespace
  "ButtonStatus_Event",  // message name
  3,  // number of fields
  sizeof(roomie_msgs::srv::ButtonStatus_Event),
  false,  // has_any_key_member_
  ButtonStatus_Event_message_member_array,  // message members
  ButtonStatus_Event_init_function,  // function to initialize message memory (memory has to be allocated)
  ButtonStatus_Event_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t ButtonStatus_Event_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ButtonStatus_Event_message_members,
  get_message_typesupport_handle_function,
  &roomie_msgs__srv__ButtonStatus_Event__get_type_hash,
  &roomie_msgs__srv__ButtonStatus_Event__get_type_description,
  &roomie_msgs__srv__ButtonStatus_Event__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace roomie_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<roomie_msgs::srv::ButtonStatus_Event>()
{
  return &::roomie_msgs::srv::rosidl_typesupport_introspection_cpp::ButtonStatus_Event_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, roomie_msgs, srv, ButtonStatus_Event)() {
  return &::roomie_msgs::srv::rosidl_typesupport_introspection_cpp::ButtonStatus_Event_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"
// already included above
// #include "roomie_msgs/srv/detail/button_status__functions.h"
// already included above
// #include "roomie_msgs/srv/detail/button_status__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/service_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/service_type_support_decl.hpp"

namespace roomie_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

// this is intentionally not const to allow initialization later to prevent an initialization race
static ::rosidl_typesupport_introspection_cpp::ServiceMembers ButtonStatus_service_members = {
  "roomie_msgs::srv",  // service namespace
  "ButtonStatus",  // service name
  // the following fields are initialized below on first access
  // see get_service_type_support_handle<roomie_msgs::srv::ButtonStatus>()
  nullptr,  // request message
  nullptr,  // response message
  nullptr,  // event message
};

static const rosidl_service_type_support_t ButtonStatus_service_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ButtonStatus_service_members,
  get_service_typesupport_handle_function,
  ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<roomie_msgs::srv::ButtonStatus_Request>(),
  ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<roomie_msgs::srv::ButtonStatus_Response>(),
  ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<roomie_msgs::srv::ButtonStatus_Event>(),
  &::rosidl_typesupport_cpp::service_create_event_message<roomie_msgs::srv::ButtonStatus>,
  &::rosidl_typesupport_cpp::service_destroy_event_message<roomie_msgs::srv::ButtonStatus>,
  &roomie_msgs__srv__ButtonStatus__get_type_hash,
  &roomie_msgs__srv__ButtonStatus__get_type_description,
  &roomie_msgs__srv__ButtonStatus__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace roomie_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<roomie_msgs::srv::ButtonStatus>()
{
  // get a handle to the value to be returned
  auto service_type_support =
    &::roomie_msgs::srv::rosidl_typesupport_introspection_cpp::ButtonStatus_service_type_support_handle;
  // get a non-const and properly typed version of the data void *
  auto service_members = const_cast<::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
    static_cast<const ::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
      service_type_support->data));
  // make sure all of the service_members are initialized
  // if they are not, initialize them
  if (
    service_members->request_members_ == nullptr ||
    service_members->response_members_ == nullptr ||
    service_members->event_members_ == nullptr)
  {
    // initialize the request_members_ with the static function from the external library
    service_members->request_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::roomie_msgs::srv::ButtonStatus_Request
      >()->data
      );
    // initialize the response_members_ with the static function from the external library
    service_members->response_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::roomie_msgs::srv::ButtonStatus_Response
      >()->data
      );
    // initialize the event_members_ with the static function from the external library
    service_members->event_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::roomie_msgs::srv::ButtonStatus_Event
      >()->data
      );
  }
  // finally return the properly initialized service_type_support handle
  return service_type_support;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, roomie_msgs, srv, ButtonStatus)() {
  return ::rosidl_typesupport_introspection_cpp::get_service_type_support_handle<roomie_msgs::srv::ButtonStatus>();
}

#ifdef __cplusplus
}
#endif
