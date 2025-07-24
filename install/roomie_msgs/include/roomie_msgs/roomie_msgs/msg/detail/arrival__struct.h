// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from roomie_msgs:msg/Arrival.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/arrival.h"


#ifndef ROOMIE_MSGS__MSG__DETAIL__ARRIVAL__STRUCT_H_
#define ROOMIE_MSGS__MSG__DETAIL__ARRIVAL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/Arrival in the package roomie_msgs.
/**
  * Arrival.msg
 */
typedef struct roomie_msgs__msg__Arrival
{
  int32_t robot_id;
  int32_t task_id;
  int32_t location_id;
} roomie_msgs__msg__Arrival;

// Struct for a sequence of roomie_msgs__msg__Arrival.
typedef struct roomie_msgs__msg__Arrival__Sequence
{
  roomie_msgs__msg__Arrival * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__msg__Arrival__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__MSG__DETAIL__ARRIVAL__STRUCT_H_
