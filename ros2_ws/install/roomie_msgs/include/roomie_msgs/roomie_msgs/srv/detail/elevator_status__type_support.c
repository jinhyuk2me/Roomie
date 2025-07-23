// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from roomie_msgs:srv/ElevatorStatus.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "roomie_msgs/srv/detail/elevator_status__rosidl_typesupport_introspection_c.h"
#include "roomie_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "roomie_msgs/srv/detail/elevator_status__functions.h"
#include "roomie_msgs/srv/detail/elevator_status__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  roomie_msgs__srv__ElevatorStatus_Request__init(message_memory);
}

void roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_fini_function(void * message_memory)
{
  roomie_msgs__srv__ElevatorStatus_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_message_member_array[1] = {
  {
    "robot_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs__srv__ElevatorStatus_Request, robot_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_message_members = {
  "roomie_msgs__srv",  // message namespace
  "ElevatorStatus_Request",  // message name
  1,  // number of fields
  sizeof(roomie_msgs__srv__ElevatorStatus_Request),
  false,  // has_any_key_member_
  roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_message_member_array,  // message members
  roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_message_type_support_handle = {
  0,
  &roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_message_members,
  get_message_typesupport_handle_function,
  &roomie_msgs__srv__ElevatorStatus_Request__get_type_hash,
  &roomie_msgs__srv__ElevatorStatus_Request__get_type_description,
  &roomie_msgs__srv__ElevatorStatus_Request__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_roomie_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, srv, ElevatorStatus_Request)() {
  if (!roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_message_type_support_handle.typesupport_identifier) {
    roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "roomie_msgs/srv/detail/elevator_status__rosidl_typesupport_introspection_c.h"
// already included above
// #include "roomie_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "roomie_msgs/srv/detail/elevator_status__functions.h"
// already included above
// #include "roomie_msgs/srv/detail/elevator_status__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  roomie_msgs__srv__ElevatorStatus_Response__init(message_memory);
}

void roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_fini_function(void * message_memory)
{
  roomie_msgs__srv__ElevatorStatus_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_message_member_array[3] = {
  {
    "robot_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs__srv__ElevatorStatus_Response, robot_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "direction",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs__srv__ElevatorStatus_Response, direction),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "position",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs__srv__ElevatorStatus_Response, position),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_message_members = {
  "roomie_msgs__srv",  // message namespace
  "ElevatorStatus_Response",  // message name
  3,  // number of fields
  sizeof(roomie_msgs__srv__ElevatorStatus_Response),
  false,  // has_any_key_member_
  roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_message_member_array,  // message members
  roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_message_type_support_handle = {
  0,
  &roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_message_members,
  get_message_typesupport_handle_function,
  &roomie_msgs__srv__ElevatorStatus_Response__get_type_hash,
  &roomie_msgs__srv__ElevatorStatus_Response__get_type_description,
  &roomie_msgs__srv__ElevatorStatus_Response__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_roomie_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, srv, ElevatorStatus_Response)() {
  if (!roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_message_type_support_handle.typesupport_identifier) {
    roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "roomie_msgs/srv/detail/elevator_status__rosidl_typesupport_introspection_c.h"
// already included above
// #include "roomie_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "roomie_msgs/srv/detail/elevator_status__functions.h"
// already included above
// #include "roomie_msgs/srv/detail/elevator_status__struct.h"


// Include directives for member types
// Member `info`
#include "service_msgs/msg/service_event_info.h"
// Member `info`
#include "service_msgs/msg/detail/service_event_info__rosidl_typesupport_introspection_c.h"
// Member `request`
// Member `response`
#include "roomie_msgs/srv/elevator_status.h"
// Member `request`
// Member `response`
// already included above
// #include "roomie_msgs/srv/detail/elevator_status__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  roomie_msgs__srv__ElevatorStatus_Event__init(message_memory);
}

void roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_fini_function(void * message_memory)
{
  roomie_msgs__srv__ElevatorStatus_Event__fini(message_memory);
}

size_t roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__size_function__ElevatorStatus_Event__request(
  const void * untyped_member)
{
  const roomie_msgs__srv__ElevatorStatus_Request__Sequence * member =
    (const roomie_msgs__srv__ElevatorStatus_Request__Sequence *)(untyped_member);
  return member->size;
}

const void * roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__get_const_function__ElevatorStatus_Event__request(
  const void * untyped_member, size_t index)
{
  const roomie_msgs__srv__ElevatorStatus_Request__Sequence * member =
    (const roomie_msgs__srv__ElevatorStatus_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void * roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__get_function__ElevatorStatus_Event__request(
  void * untyped_member, size_t index)
{
  roomie_msgs__srv__ElevatorStatus_Request__Sequence * member =
    (roomie_msgs__srv__ElevatorStatus_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__fetch_function__ElevatorStatus_Event__request(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const roomie_msgs__srv__ElevatorStatus_Request * item =
    ((const roomie_msgs__srv__ElevatorStatus_Request *)
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__get_const_function__ElevatorStatus_Event__request(untyped_member, index));
  roomie_msgs__srv__ElevatorStatus_Request * value =
    (roomie_msgs__srv__ElevatorStatus_Request *)(untyped_value);
  *value = *item;
}

void roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__assign_function__ElevatorStatus_Event__request(
  void * untyped_member, size_t index, const void * untyped_value)
{
  roomie_msgs__srv__ElevatorStatus_Request * item =
    ((roomie_msgs__srv__ElevatorStatus_Request *)
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__get_function__ElevatorStatus_Event__request(untyped_member, index));
  const roomie_msgs__srv__ElevatorStatus_Request * value =
    (const roomie_msgs__srv__ElevatorStatus_Request *)(untyped_value);
  *item = *value;
}

bool roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__resize_function__ElevatorStatus_Event__request(
  void * untyped_member, size_t size)
{
  roomie_msgs__srv__ElevatorStatus_Request__Sequence * member =
    (roomie_msgs__srv__ElevatorStatus_Request__Sequence *)(untyped_member);
  roomie_msgs__srv__ElevatorStatus_Request__Sequence__fini(member);
  return roomie_msgs__srv__ElevatorStatus_Request__Sequence__init(member, size);
}

size_t roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__size_function__ElevatorStatus_Event__response(
  const void * untyped_member)
{
  const roomie_msgs__srv__ElevatorStatus_Response__Sequence * member =
    (const roomie_msgs__srv__ElevatorStatus_Response__Sequence *)(untyped_member);
  return member->size;
}

const void * roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__get_const_function__ElevatorStatus_Event__response(
  const void * untyped_member, size_t index)
{
  const roomie_msgs__srv__ElevatorStatus_Response__Sequence * member =
    (const roomie_msgs__srv__ElevatorStatus_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void * roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__get_function__ElevatorStatus_Event__response(
  void * untyped_member, size_t index)
{
  roomie_msgs__srv__ElevatorStatus_Response__Sequence * member =
    (roomie_msgs__srv__ElevatorStatus_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__fetch_function__ElevatorStatus_Event__response(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const roomie_msgs__srv__ElevatorStatus_Response * item =
    ((const roomie_msgs__srv__ElevatorStatus_Response *)
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__get_const_function__ElevatorStatus_Event__response(untyped_member, index));
  roomie_msgs__srv__ElevatorStatus_Response * value =
    (roomie_msgs__srv__ElevatorStatus_Response *)(untyped_value);
  *value = *item;
}

void roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__assign_function__ElevatorStatus_Event__response(
  void * untyped_member, size_t index, const void * untyped_value)
{
  roomie_msgs__srv__ElevatorStatus_Response * item =
    ((roomie_msgs__srv__ElevatorStatus_Response *)
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__get_function__ElevatorStatus_Event__response(untyped_member, index));
  const roomie_msgs__srv__ElevatorStatus_Response * value =
    (const roomie_msgs__srv__ElevatorStatus_Response *)(untyped_value);
  *item = *value;
}

bool roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__resize_function__ElevatorStatus_Event__response(
  void * untyped_member, size_t size)
{
  roomie_msgs__srv__ElevatorStatus_Response__Sequence * member =
    (roomie_msgs__srv__ElevatorStatus_Response__Sequence *)(untyped_member);
  roomie_msgs__srv__ElevatorStatus_Response__Sequence__fini(member);
  return roomie_msgs__srv__ElevatorStatus_Response__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_message_member_array[3] = {
  {
    "info",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs__srv__ElevatorStatus_Event, info),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "request",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(roomie_msgs__srv__ElevatorStatus_Event, request),  // bytes offset in struct
    NULL,  // default value
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__size_function__ElevatorStatus_Event__request,  // size() function pointer
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__get_const_function__ElevatorStatus_Event__request,  // get_const(index) function pointer
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__get_function__ElevatorStatus_Event__request,  // get(index) function pointer
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__fetch_function__ElevatorStatus_Event__request,  // fetch(index, &value) function pointer
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__assign_function__ElevatorStatus_Event__request,  // assign(index, value) function pointer
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__resize_function__ElevatorStatus_Event__request  // resize(index) function pointer
  },
  {
    "response",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(roomie_msgs__srv__ElevatorStatus_Event, response),  // bytes offset in struct
    NULL,  // default value
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__size_function__ElevatorStatus_Event__response,  // size() function pointer
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__get_const_function__ElevatorStatus_Event__response,  // get_const(index) function pointer
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__get_function__ElevatorStatus_Event__response,  // get(index) function pointer
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__fetch_function__ElevatorStatus_Event__response,  // fetch(index, &value) function pointer
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__assign_function__ElevatorStatus_Event__response,  // assign(index, value) function pointer
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__resize_function__ElevatorStatus_Event__response  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_message_members = {
  "roomie_msgs__srv",  // message namespace
  "ElevatorStatus_Event",  // message name
  3,  // number of fields
  sizeof(roomie_msgs__srv__ElevatorStatus_Event),
  false,  // has_any_key_member_
  roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_message_member_array,  // message members
  roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_init_function,  // function to initialize message memory (memory has to be allocated)
  roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_message_type_support_handle = {
  0,
  &roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_message_members,
  get_message_typesupport_handle_function,
  &roomie_msgs__srv__ElevatorStatus_Event__get_type_hash,
  &roomie_msgs__srv__ElevatorStatus_Event__get_type_description,
  &roomie_msgs__srv__ElevatorStatus_Event__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_roomie_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, srv, ElevatorStatus_Event)() {
  roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_msgs, msg, ServiceEventInfo)();
  roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, srv, ElevatorStatus_Request)();
  roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, srv, ElevatorStatus_Response)();
  if (!roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_message_type_support_handle.typesupport_identifier) {
    roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "roomie_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "roomie_msgs/srv/detail/elevator_status__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers roomie_msgs__srv__detail__elevator_status__rosidl_typesupport_introspection_c__ElevatorStatus_service_members = {
  "roomie_msgs__srv",  // service namespace
  "ElevatorStatus",  // service name
  // the following fields are initialized below on first access
  NULL,  // request message
  // roomie_msgs__srv__detail__elevator_status__rosidl_typesupport_introspection_c__ElevatorStatus_Request_message_type_support_handle,
  NULL,  // response message
  // roomie_msgs__srv__detail__elevator_status__rosidl_typesupport_introspection_c__ElevatorStatus_Response_message_type_support_handle
  NULL  // event_message
  // roomie_msgs__srv__detail__elevator_status__rosidl_typesupport_introspection_c__ElevatorStatus_Response_message_type_support_handle
};


static rosidl_service_type_support_t roomie_msgs__srv__detail__elevator_status__rosidl_typesupport_introspection_c__ElevatorStatus_service_type_support_handle = {
  0,
  &roomie_msgs__srv__detail__elevator_status__rosidl_typesupport_introspection_c__ElevatorStatus_service_members,
  get_service_typesupport_handle_function,
  &roomie_msgs__srv__ElevatorStatus_Request__rosidl_typesupport_introspection_c__ElevatorStatus_Request_message_type_support_handle,
  &roomie_msgs__srv__ElevatorStatus_Response__rosidl_typesupport_introspection_c__ElevatorStatus_Response_message_type_support_handle,
  &roomie_msgs__srv__ElevatorStatus_Event__rosidl_typesupport_introspection_c__ElevatorStatus_Event_message_type_support_handle,
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    roomie_msgs,
    srv,
    ElevatorStatus
  ),
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    roomie_msgs,
    srv,
    ElevatorStatus
  ),
  &roomie_msgs__srv__ElevatorStatus__get_type_hash,
  &roomie_msgs__srv__ElevatorStatus__get_type_description,
  &roomie_msgs__srv__ElevatorStatus__get_type_description_sources,
};

// Forward declaration of message type support functions for service members
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, srv, ElevatorStatus_Request)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, srv, ElevatorStatus_Response)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, srv, ElevatorStatus_Event)(void);

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_roomie_msgs
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, srv, ElevatorStatus)(void) {
  if (!roomie_msgs__srv__detail__elevator_status__rosidl_typesupport_introspection_c__ElevatorStatus_service_type_support_handle.typesupport_identifier) {
    roomie_msgs__srv__detail__elevator_status__rosidl_typesupport_introspection_c__ElevatorStatus_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)roomie_msgs__srv__detail__elevator_status__rosidl_typesupport_introspection_c__ElevatorStatus_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, srv, ElevatorStatus_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, srv, ElevatorStatus_Response)()->data;
  }
  if (!service_members->event_members_) {
    service_members->event_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, srv, ElevatorStatus_Event)()->data;
  }

  return &roomie_msgs__srv__detail__elevator_status__rosidl_typesupport_introspection_c__ElevatorStatus_service_type_support_handle;
}
