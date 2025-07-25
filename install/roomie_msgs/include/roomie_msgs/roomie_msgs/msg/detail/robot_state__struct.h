// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from roomie_msgs:msg/RobotState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/robot_state.h"


#ifndef ROOMIE_MSGS__MSG__DETAIL__ROBOT_STATE__STRUCT_H_
#define ROOMIE_MSGS__MSG__DETAIL__ROBOT_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/RobotState in the package roomie_msgs.
/**
  * RobotState.msg
 */
typedef struct roomie_msgs__msg__RobotState
{
  int32_t robot_id;
  int32_t robot_state_id;
} roomie_msgs__msg__RobotState;

// Struct for a sequence of roomie_msgs__msg__RobotState.
typedef struct roomie_msgs__msg__RobotState__Sequence
{
  roomie_msgs__msg__RobotState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__msg__RobotState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__MSG__DETAIL__ROBOT_STATE__STRUCT_H_
