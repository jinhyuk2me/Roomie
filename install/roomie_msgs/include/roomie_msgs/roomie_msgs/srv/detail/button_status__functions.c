// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from roomie_msgs:srv/ButtonStatus.idl
// generated code does not contain a copyright notice
#include "roomie_msgs/srv/detail/button_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `button_ids`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
roomie_msgs__srv__ButtonStatus_Request__init(roomie_msgs__srv__ButtonStatus_Request * msg)
{
  if (!msg) {
    return false;
  }
  // robot_id
  // button_ids
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->button_ids, 0)) {
    roomie_msgs__srv__ButtonStatus_Request__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__srv__ButtonStatus_Request__fini(roomie_msgs__srv__ButtonStatus_Request * msg)
{
  if (!msg) {
    return;
  }
  // robot_id
  // button_ids
  rosidl_runtime_c__int32__Sequence__fini(&msg->button_ids);
}

bool
roomie_msgs__srv__ButtonStatus_Request__are_equal(const roomie_msgs__srv__ButtonStatus_Request * lhs, const roomie_msgs__srv__ButtonStatus_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_id
  if (lhs->robot_id != rhs->robot_id) {
    return false;
  }
  // button_ids
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->button_ids), &(rhs->button_ids)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__srv__ButtonStatus_Request__copy(
  const roomie_msgs__srv__ButtonStatus_Request * input,
  roomie_msgs__srv__ButtonStatus_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // button_ids
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->button_ids), &(output->button_ids)))
  {
    return false;
  }
  return true;
}

roomie_msgs__srv__ButtonStatus_Request *
roomie_msgs__srv__ButtonStatus_Request__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ButtonStatus_Request * msg = (roomie_msgs__srv__ButtonStatus_Request *)allocator.allocate(sizeof(roomie_msgs__srv__ButtonStatus_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__srv__ButtonStatus_Request));
  bool success = roomie_msgs__srv__ButtonStatus_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__srv__ButtonStatus_Request__destroy(roomie_msgs__srv__ButtonStatus_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__srv__ButtonStatus_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__srv__ButtonStatus_Request__Sequence__init(roomie_msgs__srv__ButtonStatus_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ButtonStatus_Request * data = NULL;

  if (size) {
    data = (roomie_msgs__srv__ButtonStatus_Request *)allocator.zero_allocate(size, sizeof(roomie_msgs__srv__ButtonStatus_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__srv__ButtonStatus_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__srv__ButtonStatus_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
roomie_msgs__srv__ButtonStatus_Request__Sequence__fini(roomie_msgs__srv__ButtonStatus_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      roomie_msgs__srv__ButtonStatus_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

roomie_msgs__srv__ButtonStatus_Request__Sequence *
roomie_msgs__srv__ButtonStatus_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ButtonStatus_Request__Sequence * array = (roomie_msgs__srv__ButtonStatus_Request__Sequence *)allocator.allocate(sizeof(roomie_msgs__srv__ButtonStatus_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__srv__ButtonStatus_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__srv__ButtonStatus_Request__Sequence__destroy(roomie_msgs__srv__ButtonStatus_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__srv__ButtonStatus_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__srv__ButtonStatus_Request__Sequence__are_equal(const roomie_msgs__srv__ButtonStatus_Request__Sequence * lhs, const roomie_msgs__srv__ButtonStatus_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__srv__ButtonStatus_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__srv__ButtonStatus_Request__Sequence__copy(
  const roomie_msgs__srv__ButtonStatus_Request__Sequence * input,
  roomie_msgs__srv__ButtonStatus_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__srv__ButtonStatus_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__srv__ButtonStatus_Request * data =
      (roomie_msgs__srv__ButtonStatus_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__srv__ButtonStatus_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__srv__ButtonStatus_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__srv__ButtonStatus_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `xs`
// Member `ys`
// Member `depths`
// Member `is_pressed`
// already included above
// #include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `timestamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
roomie_msgs__srv__ButtonStatus_Response__init(roomie_msgs__srv__ButtonStatus_Response * msg)
{
  if (!msg) {
    return false;
  }
  // robot_id
  // success
  // xs
  if (!rosidl_runtime_c__float__Sequence__init(&msg->xs, 0)) {
    roomie_msgs__srv__ButtonStatus_Response__fini(msg);
    return false;
  }
  // ys
  if (!rosidl_runtime_c__float__Sequence__init(&msg->ys, 0)) {
    roomie_msgs__srv__ButtonStatus_Response__fini(msg);
    return false;
  }
  // depths
  if (!rosidl_runtime_c__float__Sequence__init(&msg->depths, 0)) {
    roomie_msgs__srv__ButtonStatus_Response__fini(msg);
    return false;
  }
  // is_pressed
  if (!rosidl_runtime_c__boolean__Sequence__init(&msg->is_pressed, 0)) {
    roomie_msgs__srv__ButtonStatus_Response__fini(msg);
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__Sequence__init(&msg->timestamp, 0)) {
    roomie_msgs__srv__ButtonStatus_Response__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__srv__ButtonStatus_Response__fini(roomie_msgs__srv__ButtonStatus_Response * msg)
{
  if (!msg) {
    return;
  }
  // robot_id
  // success
  // xs
  rosidl_runtime_c__float__Sequence__fini(&msg->xs);
  // ys
  rosidl_runtime_c__float__Sequence__fini(&msg->ys);
  // depths
  rosidl_runtime_c__float__Sequence__fini(&msg->depths);
  // is_pressed
  rosidl_runtime_c__boolean__Sequence__fini(&msg->is_pressed);
  // timestamp
  builtin_interfaces__msg__Time__Sequence__fini(&msg->timestamp);
}

bool
roomie_msgs__srv__ButtonStatus_Response__are_equal(const roomie_msgs__srv__ButtonStatus_Response * lhs, const roomie_msgs__srv__ButtonStatus_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_id
  if (lhs->robot_id != rhs->robot_id) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // xs
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->xs), &(rhs->xs)))
  {
    return false;
  }
  // ys
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->ys), &(rhs->ys)))
  {
    return false;
  }
  // depths
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->depths), &(rhs->depths)))
  {
    return false;
  }
  // is_pressed
  if (!rosidl_runtime_c__boolean__Sequence__are_equal(
      &(lhs->is_pressed), &(rhs->is_pressed)))
  {
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__Sequence__are_equal(
      &(lhs->timestamp), &(rhs->timestamp)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__srv__ButtonStatus_Response__copy(
  const roomie_msgs__srv__ButtonStatus_Response * input,
  roomie_msgs__srv__ButtonStatus_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // success
  output->success = input->success;
  // xs
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->xs), &(output->xs)))
  {
    return false;
  }
  // ys
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->ys), &(output->ys)))
  {
    return false;
  }
  // depths
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->depths), &(output->depths)))
  {
    return false;
  }
  // is_pressed
  if (!rosidl_runtime_c__boolean__Sequence__copy(
      &(input->is_pressed), &(output->is_pressed)))
  {
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__Sequence__copy(
      &(input->timestamp), &(output->timestamp)))
  {
    return false;
  }
  return true;
}

roomie_msgs__srv__ButtonStatus_Response *
roomie_msgs__srv__ButtonStatus_Response__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ButtonStatus_Response * msg = (roomie_msgs__srv__ButtonStatus_Response *)allocator.allocate(sizeof(roomie_msgs__srv__ButtonStatus_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__srv__ButtonStatus_Response));
  bool success = roomie_msgs__srv__ButtonStatus_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__srv__ButtonStatus_Response__destroy(roomie_msgs__srv__ButtonStatus_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__srv__ButtonStatus_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__srv__ButtonStatus_Response__Sequence__init(roomie_msgs__srv__ButtonStatus_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ButtonStatus_Response * data = NULL;

  if (size) {
    data = (roomie_msgs__srv__ButtonStatus_Response *)allocator.zero_allocate(size, sizeof(roomie_msgs__srv__ButtonStatus_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__srv__ButtonStatus_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__srv__ButtonStatus_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
roomie_msgs__srv__ButtonStatus_Response__Sequence__fini(roomie_msgs__srv__ButtonStatus_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      roomie_msgs__srv__ButtonStatus_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

roomie_msgs__srv__ButtonStatus_Response__Sequence *
roomie_msgs__srv__ButtonStatus_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ButtonStatus_Response__Sequence * array = (roomie_msgs__srv__ButtonStatus_Response__Sequence *)allocator.allocate(sizeof(roomie_msgs__srv__ButtonStatus_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__srv__ButtonStatus_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__srv__ButtonStatus_Response__Sequence__destroy(roomie_msgs__srv__ButtonStatus_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__srv__ButtonStatus_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__srv__ButtonStatus_Response__Sequence__are_equal(const roomie_msgs__srv__ButtonStatus_Response__Sequence * lhs, const roomie_msgs__srv__ButtonStatus_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__srv__ButtonStatus_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__srv__ButtonStatus_Response__Sequence__copy(
  const roomie_msgs__srv__ButtonStatus_Response__Sequence * input,
  roomie_msgs__srv__ButtonStatus_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__srv__ButtonStatus_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__srv__ButtonStatus_Response * data =
      (roomie_msgs__srv__ButtonStatus_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__srv__ButtonStatus_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__srv__ButtonStatus_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__srv__ButtonStatus_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `info`
#include "service_msgs/msg/detail/service_event_info__functions.h"
// Member `request`
// Member `response`
// already included above
// #include "roomie_msgs/srv/detail/button_status__functions.h"

bool
roomie_msgs__srv__ButtonStatus_Event__init(roomie_msgs__srv__ButtonStatus_Event * msg)
{
  if (!msg) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__init(&msg->info)) {
    roomie_msgs__srv__ButtonStatus_Event__fini(msg);
    return false;
  }
  // request
  if (!roomie_msgs__srv__ButtonStatus_Request__Sequence__init(&msg->request, 0)) {
    roomie_msgs__srv__ButtonStatus_Event__fini(msg);
    return false;
  }
  // response
  if (!roomie_msgs__srv__ButtonStatus_Response__Sequence__init(&msg->response, 0)) {
    roomie_msgs__srv__ButtonStatus_Event__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__srv__ButtonStatus_Event__fini(roomie_msgs__srv__ButtonStatus_Event * msg)
{
  if (!msg) {
    return;
  }
  // info
  service_msgs__msg__ServiceEventInfo__fini(&msg->info);
  // request
  roomie_msgs__srv__ButtonStatus_Request__Sequence__fini(&msg->request);
  // response
  roomie_msgs__srv__ButtonStatus_Response__Sequence__fini(&msg->response);
}

bool
roomie_msgs__srv__ButtonStatus_Event__are_equal(const roomie_msgs__srv__ButtonStatus_Event * lhs, const roomie_msgs__srv__ButtonStatus_Event * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__are_equal(
      &(lhs->info), &(rhs->info)))
  {
    return false;
  }
  // request
  if (!roomie_msgs__srv__ButtonStatus_Request__Sequence__are_equal(
      &(lhs->request), &(rhs->request)))
  {
    return false;
  }
  // response
  if (!roomie_msgs__srv__ButtonStatus_Response__Sequence__are_equal(
      &(lhs->response), &(rhs->response)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__srv__ButtonStatus_Event__copy(
  const roomie_msgs__srv__ButtonStatus_Event * input,
  roomie_msgs__srv__ButtonStatus_Event * output)
{
  if (!input || !output) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__copy(
      &(input->info), &(output->info)))
  {
    return false;
  }
  // request
  if (!roomie_msgs__srv__ButtonStatus_Request__Sequence__copy(
      &(input->request), &(output->request)))
  {
    return false;
  }
  // response
  if (!roomie_msgs__srv__ButtonStatus_Response__Sequence__copy(
      &(input->response), &(output->response)))
  {
    return false;
  }
  return true;
}

roomie_msgs__srv__ButtonStatus_Event *
roomie_msgs__srv__ButtonStatus_Event__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ButtonStatus_Event * msg = (roomie_msgs__srv__ButtonStatus_Event *)allocator.allocate(sizeof(roomie_msgs__srv__ButtonStatus_Event), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__srv__ButtonStatus_Event));
  bool success = roomie_msgs__srv__ButtonStatus_Event__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__srv__ButtonStatus_Event__destroy(roomie_msgs__srv__ButtonStatus_Event * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__srv__ButtonStatus_Event__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__srv__ButtonStatus_Event__Sequence__init(roomie_msgs__srv__ButtonStatus_Event__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ButtonStatus_Event * data = NULL;

  if (size) {
    data = (roomie_msgs__srv__ButtonStatus_Event *)allocator.zero_allocate(size, sizeof(roomie_msgs__srv__ButtonStatus_Event), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__srv__ButtonStatus_Event__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__srv__ButtonStatus_Event__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
roomie_msgs__srv__ButtonStatus_Event__Sequence__fini(roomie_msgs__srv__ButtonStatus_Event__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      roomie_msgs__srv__ButtonStatus_Event__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

roomie_msgs__srv__ButtonStatus_Event__Sequence *
roomie_msgs__srv__ButtonStatus_Event__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ButtonStatus_Event__Sequence * array = (roomie_msgs__srv__ButtonStatus_Event__Sequence *)allocator.allocate(sizeof(roomie_msgs__srv__ButtonStatus_Event__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__srv__ButtonStatus_Event__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__srv__ButtonStatus_Event__Sequence__destroy(roomie_msgs__srv__ButtonStatus_Event__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__srv__ButtonStatus_Event__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__srv__ButtonStatus_Event__Sequence__are_equal(const roomie_msgs__srv__ButtonStatus_Event__Sequence * lhs, const roomie_msgs__srv__ButtonStatus_Event__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__srv__ButtonStatus_Event__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__srv__ButtonStatus_Event__Sequence__copy(
  const roomie_msgs__srv__ButtonStatus_Event__Sequence * input,
  roomie_msgs__srv__ButtonStatus_Event__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__srv__ButtonStatus_Event);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__srv__ButtonStatus_Event * data =
      (roomie_msgs__srv__ButtonStatus_Event *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__srv__ButtonStatus_Event__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__srv__ButtonStatus_Event__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__srv__ButtonStatus_Event__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
