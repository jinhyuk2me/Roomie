// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from roomie_msgs:msg/PickupCompleted.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "roomie_msgs/msg/detail/pickup_completed__rosidl_typesupport_introspection_c.h"
#include "roomie_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "roomie_msgs/msg/detail/pickup_completed__functions.h"
#include "roomie_msgs/msg/detail/pickup_completed__struct.h"


// Include directives for member types
// Member `timestamp`
#include "builtin_interfaces/msg/time.h"
// Member `timestamp`
#include "builtin_interfaces/msg/detail/time__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  roomie_msgs__msg__PickupCompleted__init(message_memory);
}

void roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_fini_function(void * message_memory)
{
  roomie_msgs__msg__PickupCompleted__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_message_member_array[3] = {
  {
    "robot_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs__msg__PickupCompleted, robot_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "task_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs__msg__PickupCompleted, task_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "timestamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(roomie_msgs__msg__PickupCompleted, timestamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_message_members = {
  "roomie_msgs__msg",  // message namespace
  "PickupCompleted",  // message name
  3,  // number of fields
  sizeof(roomie_msgs__msg__PickupCompleted),
  false,  // has_any_key_member_
  roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_message_member_array,  // message members
  roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_init_function,  // function to initialize message memory (memory has to be allocated)
  roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_message_type_support_handle = {
  0,
  &roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_message_members,
  get_message_typesupport_handle_function,
  &roomie_msgs__msg__PickupCompleted__get_type_hash,
  &roomie_msgs__msg__PickupCompleted__get_type_description,
  &roomie_msgs__msg__PickupCompleted__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_roomie_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, roomie_msgs, msg, PickupCompleted)() {
  roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  if (!roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_message_type_support_handle.typesupport_identifier) {
    roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &roomie_msgs__msg__PickupCompleted__rosidl_typesupport_introspection_c__PickupCompleted_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
