// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from roomie_msgs:msg/TrackingEvent.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/msg/tracking_event.h"


#ifndef ROOMIE_MSGS__MSG__DETAIL__TRACKING_EVENT__FUNCTIONS_H_
#define ROOMIE_MSGS__MSG__DETAIL__TRACKING_EVENT__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/action_type_support_struct.h"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_runtime_c/service_type_support_struct.h"
#include "rosidl_runtime_c/type_description/type_description__struct.h"
#include "rosidl_runtime_c/type_description/type_source__struct.h"
#include "rosidl_runtime_c/type_hash.h"
#include "rosidl_runtime_c/visibility_control.h"
#include "roomie_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "roomie_msgs/msg/detail/tracking_event__struct.h"

/// Initialize msg/TrackingEvent message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * roomie_msgs__msg__TrackingEvent
 * )) before or use
 * roomie_msgs__msg__TrackingEvent__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
bool
roomie_msgs__msg__TrackingEvent__init(roomie_msgs__msg__TrackingEvent * msg);

/// Finalize msg/TrackingEvent message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
void
roomie_msgs__msg__TrackingEvent__fini(roomie_msgs__msg__TrackingEvent * msg);

/// Create msg/TrackingEvent message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * roomie_msgs__msg__TrackingEvent__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
roomie_msgs__msg__TrackingEvent *
roomie_msgs__msg__TrackingEvent__create(void);

/// Destroy msg/TrackingEvent message.
/**
 * It calls
 * roomie_msgs__msg__TrackingEvent__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
void
roomie_msgs__msg__TrackingEvent__destroy(roomie_msgs__msg__TrackingEvent * msg);

/// Check for msg/TrackingEvent message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
bool
roomie_msgs__msg__TrackingEvent__are_equal(const roomie_msgs__msg__TrackingEvent * lhs, const roomie_msgs__msg__TrackingEvent * rhs);

/// Copy a msg/TrackingEvent message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
bool
roomie_msgs__msg__TrackingEvent__copy(
  const roomie_msgs__msg__TrackingEvent * input,
  roomie_msgs__msg__TrackingEvent * output);

/// Retrieve pointer to the hash of the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__msg__TrackingEvent__get_type_hash(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__msg__TrackingEvent__get_type_description(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the single raw source text that defined this type.
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__msg__TrackingEvent__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the recursive raw sources that defined the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__msg__TrackingEvent__get_type_description_sources(
  const rosidl_message_type_support_t * type_support);

/// Initialize array of msg/TrackingEvent messages.
/**
 * It allocates the memory for the number of elements and calls
 * roomie_msgs__msg__TrackingEvent__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
bool
roomie_msgs__msg__TrackingEvent__Sequence__init(roomie_msgs__msg__TrackingEvent__Sequence * array, size_t size);

/// Finalize array of msg/TrackingEvent messages.
/**
 * It calls
 * roomie_msgs__msg__TrackingEvent__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
void
roomie_msgs__msg__TrackingEvent__Sequence__fini(roomie_msgs__msg__TrackingEvent__Sequence * array);

/// Create array of msg/TrackingEvent messages.
/**
 * It allocates the memory for the array and calls
 * roomie_msgs__msg__TrackingEvent__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
roomie_msgs__msg__TrackingEvent__Sequence *
roomie_msgs__msg__TrackingEvent__Sequence__create(size_t size);

/// Destroy array of msg/TrackingEvent messages.
/**
 * It calls
 * roomie_msgs__msg__TrackingEvent__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
void
roomie_msgs__msg__TrackingEvent__Sequence__destroy(roomie_msgs__msg__TrackingEvent__Sequence * array);

/// Check for msg/TrackingEvent message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
bool
roomie_msgs__msg__TrackingEvent__Sequence__are_equal(const roomie_msgs__msg__TrackingEvent__Sequence * lhs, const roomie_msgs__msg__TrackingEvent__Sequence * rhs);

/// Copy an array of msg/TrackingEvent messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
bool
roomie_msgs__msg__TrackingEvent__Sequence__copy(
  const roomie_msgs__msg__TrackingEvent__Sequence * input,
  roomie_msgs__msg__TrackingEvent__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__MSG__DETAIL__TRACKING_EVENT__FUNCTIONS_H_
