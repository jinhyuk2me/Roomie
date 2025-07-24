// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from roomie_msgs:srv/GetLocations.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/srv/get_locations.h"


#ifndef ROOMIE_MSGS__SRV__DETAIL__GET_LOCATIONS__STRUCT_H_
#define ROOMIE_MSGS__SRV__DETAIL__GET_LOCATIONS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GetLocations in the package roomie_msgs.
typedef struct roomie_msgs__srv__GetLocations_Request
{
  int32_t robot_id;
} roomie_msgs__srv__GetLocations_Request;

// Struct for a sequence of roomie_msgs__srv__GetLocations_Request.
typedef struct roomie_msgs__srv__GetLocations_Request__Sequence
{
  roomie_msgs__srv__GetLocations_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__srv__GetLocations_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'location_ids'
// Member 'floor_ids'
// Member 'location_xs'
// Member 'location_ys'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/GetLocations in the package roomie_msgs.
typedef struct roomie_msgs__srv__GetLocations_Response
{
  int32_t robot_id;
  bool success;
  rosidl_runtime_c__int32__Sequence location_ids;
  rosidl_runtime_c__int32__Sequence floor_ids;
  rosidl_runtime_c__float__Sequence location_xs;
  rosidl_runtime_c__float__Sequence location_ys;
} roomie_msgs__srv__GetLocations_Response;

// Struct for a sequence of roomie_msgs__srv__GetLocations_Response.
typedef struct roomie_msgs__srv__GetLocations_Response__Sequence
{
  roomie_msgs__srv__GetLocations_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__srv__GetLocations_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  roomie_msgs__srv__GetLocations_Event__request__MAX_SIZE = 1
};
// response
enum
{
  roomie_msgs__srv__GetLocations_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/GetLocations in the package roomie_msgs.
typedef struct roomie_msgs__srv__GetLocations_Event
{
  service_msgs__msg__ServiceEventInfo info;
  roomie_msgs__srv__GetLocations_Request__Sequence request;
  roomie_msgs__srv__GetLocations_Response__Sequence response;
} roomie_msgs__srv__GetLocations_Event;

// Struct for a sequence of roomie_msgs__srv__GetLocations_Event.
typedef struct roomie_msgs__srv__GetLocations_Event__Sequence
{
  roomie_msgs__srv__GetLocations_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} roomie_msgs__srv__GetLocations_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROOMIE_MSGS__SRV__DETAIL__GET_LOCATIONS__STRUCT_H_
