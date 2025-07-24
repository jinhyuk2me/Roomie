// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from roomie_msgs:msg/PickupCompleted.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/pickup_completed.h"


#ifndef ROOMIE_MSGS__MSG__DETAIL__PICKUP_COMPLETED__STRUCT_H_
#define ROOMIE_MSGS__MSG__DETAIL__PICKUP_COMPLETED__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in msg/PickupCompleted in the package roomie_msgs.
/**
  * PickupCompleted.msg
 */
typedef struct roomie_msgs__msg__PickupCompleted
{
  int32_t robot_id;
  int32_t task_id;
  builtin_interfaces__msg__Time timestamp;
} roomie_msgs__msg__PickupCompleted;

// Struct for a sequence of roomie_msgs__msg__PickupCompleted.
typedef struct roomie_msgs__msg__PickupCompleted__Sequence
{
  roomie_msgs__msg__PickupCompleted * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__msg__PickupCompleted__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__MSG__DETAIL__PICKUP_COMPLETED__STRUCT_H_
