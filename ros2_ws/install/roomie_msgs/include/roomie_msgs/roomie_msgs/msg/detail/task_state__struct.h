// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from roomie_msgs:msg/TaskState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/task_state.h"


#ifndef ROOMIE_MSGS__MSG__DETAIL__TASK_STATE__STRUCT_H_
#define ROOMIE_MSGS__MSG__DETAIL__TASK_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/TaskState in the package roomie_msgs.
/**
  * TaskState.msg
 */
typedef struct roomie_msgs__msg__TaskState
{
  int32_t task_id;
  int32_t task_state_id;
} roomie_msgs__msg__TaskState;

// Struct for a sequence of roomie_msgs__msg__TaskState.
typedef struct roomie_msgs__msg__TaskState__Sequence
{
  roomie_msgs__msg__TaskState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__msg__TaskState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__MSG__DETAIL__TASK_STATE__STRUCT_H_
