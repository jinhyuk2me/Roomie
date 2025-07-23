// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from roomie_msgs:msg/TaskState.idl
// generated code does not contain a copyright notice
#ifndef ROOMIE_MSGS__MSG__DETAIL__TASK_STATE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define ROOMIE_MSGS__MSG__DETAIL__TASK_STATE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "roomie_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "roomie_msgs/msg/detail/task_state__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_roomie_msgs
bool cdr_serialize_roomie_msgs__msg__TaskState(
  const roomie_msgs__msg__TaskState * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_roomie_msgs
bool cdr_deserialize_roomie_msgs__msg__TaskState(
  eprosima::fastcdr::Cdr &,
  roomie_msgs__msg__TaskState * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_roomie_msgs
size_t get_serialized_size_roomie_msgs__msg__TaskState(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_roomie_msgs
size_t max_serialized_size_roomie_msgs__msg__TaskState(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_roomie_msgs
bool cdr_serialize_key_roomie_msgs__msg__TaskState(
  const roomie_msgs__msg__TaskState * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_roomie_msgs
size_t get_serialized_size_key_roomie_msgs__msg__TaskState(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_roomie_msgs
size_t max_serialized_size_key_roomie_msgs__msg__TaskState(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_roomie_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, roomie_msgs, msg, TaskState)();

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__MSG__DETAIL__TASK_STATE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
