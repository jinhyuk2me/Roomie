// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from roomie_msgs:srv/ControlLock.idl
// generated code does not contain a copyright notice
#include "roomie_msgs/srv/detail/control_lock__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
roomie_msgs__srv__ControlLock_Request__init(roomie_msgs__srv__ControlLock_Request * msg)
{
  if (!msg) {
    return false;
  }
  // robot_id
  // locked
  return true;
}

void
roomie_msgs__srv__ControlLock_Request__fini(roomie_msgs__srv__ControlLock_Request * msg)
{
  if (!msg) {
    return;
  }
  // robot_id
  // locked
}

bool
roomie_msgs__srv__ControlLock_Request__are_equal(const roomie_msgs__srv__ControlLock_Request * lhs, const roomie_msgs__srv__ControlLock_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_id
  if (lhs->robot_id != rhs->robot_id) {
    return false;
  }
  // locked
  if (lhs->locked != rhs->locked) {
    return false;
  }
  return true;
}

bool
roomie_msgs__srv__ControlLock_Request__copy(
  const roomie_msgs__srv__ControlLock_Request * input,
  roomie_msgs__srv__ControlLock_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // locked
  output->locked = input->locked;
  return true;
}

roomie_msgs__srv__ControlLock_Request *
roomie_msgs__srv__ControlLock_Request__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ControlLock_Request * msg = (roomie_msgs__srv__ControlLock_Request *)allocator.allocate(sizeof(roomie_msgs__srv__ControlLock_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__srv__ControlLock_Request));
  bool success = roomie_msgs__srv__ControlLock_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__srv__ControlLock_Request__destroy(roomie_msgs__srv__ControlLock_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__srv__ControlLock_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__srv__ControlLock_Request__Sequence__init(roomie_msgs__srv__ControlLock_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ControlLock_Request * data = NULL;

  if (size) {
    data = (roomie_msgs__srv__ControlLock_Request *)allocator.zero_allocate(size, sizeof(roomie_msgs__srv__ControlLock_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__srv__ControlLock_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__srv__ControlLock_Request__fini(&data[i - 1]);
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
roomie_msgs__srv__ControlLock_Request__Sequence__fini(roomie_msgs__srv__ControlLock_Request__Sequence * array)
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
      roomie_msgs__srv__ControlLock_Request__fini(&array->data[i]);
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

roomie_msgs__srv__ControlLock_Request__Sequence *
roomie_msgs__srv__ControlLock_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ControlLock_Request__Sequence * array = (roomie_msgs__srv__ControlLock_Request__Sequence *)allocator.allocate(sizeof(roomie_msgs__srv__ControlLock_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__srv__ControlLock_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__srv__ControlLock_Request__Sequence__destroy(roomie_msgs__srv__ControlLock_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__srv__ControlLock_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__srv__ControlLock_Request__Sequence__are_equal(const roomie_msgs__srv__ControlLock_Request__Sequence * lhs, const roomie_msgs__srv__ControlLock_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__srv__ControlLock_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__srv__ControlLock_Request__Sequence__copy(
  const roomie_msgs__srv__ControlLock_Request__Sequence * input,
  roomie_msgs__srv__ControlLock_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__srv__ControlLock_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__srv__ControlLock_Request * data =
      (roomie_msgs__srv__ControlLock_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__srv__ControlLock_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__srv__ControlLock_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__srv__ControlLock_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
roomie_msgs__srv__ControlLock_Response__init(roomie_msgs__srv__ControlLock_Response * msg)
{
  if (!msg) {
    return false;
  }
  // robot_id
  // success
  return true;
}

void
roomie_msgs__srv__ControlLock_Response__fini(roomie_msgs__srv__ControlLock_Response * msg)
{
  if (!msg) {
    return;
  }
  // robot_id
  // success
}

bool
roomie_msgs__srv__ControlLock_Response__are_equal(const roomie_msgs__srv__ControlLock_Response * lhs, const roomie_msgs__srv__ControlLock_Response * rhs)
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
  return true;
}

bool
roomie_msgs__srv__ControlLock_Response__copy(
  const roomie_msgs__srv__ControlLock_Response * input,
  roomie_msgs__srv__ControlLock_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // success
  output->success = input->success;
  return true;
}

roomie_msgs__srv__ControlLock_Response *
roomie_msgs__srv__ControlLock_Response__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ControlLock_Response * msg = (roomie_msgs__srv__ControlLock_Response *)allocator.allocate(sizeof(roomie_msgs__srv__ControlLock_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__srv__ControlLock_Response));
  bool success = roomie_msgs__srv__ControlLock_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__srv__ControlLock_Response__destroy(roomie_msgs__srv__ControlLock_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__srv__ControlLock_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__srv__ControlLock_Response__Sequence__init(roomie_msgs__srv__ControlLock_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ControlLock_Response * data = NULL;

  if (size) {
    data = (roomie_msgs__srv__ControlLock_Response *)allocator.zero_allocate(size, sizeof(roomie_msgs__srv__ControlLock_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__srv__ControlLock_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__srv__ControlLock_Response__fini(&data[i - 1]);
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
roomie_msgs__srv__ControlLock_Response__Sequence__fini(roomie_msgs__srv__ControlLock_Response__Sequence * array)
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
      roomie_msgs__srv__ControlLock_Response__fini(&array->data[i]);
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

roomie_msgs__srv__ControlLock_Response__Sequence *
roomie_msgs__srv__ControlLock_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ControlLock_Response__Sequence * array = (roomie_msgs__srv__ControlLock_Response__Sequence *)allocator.allocate(sizeof(roomie_msgs__srv__ControlLock_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__srv__ControlLock_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__srv__ControlLock_Response__Sequence__destroy(roomie_msgs__srv__ControlLock_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__srv__ControlLock_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__srv__ControlLock_Response__Sequence__are_equal(const roomie_msgs__srv__ControlLock_Response__Sequence * lhs, const roomie_msgs__srv__ControlLock_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__srv__ControlLock_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__srv__ControlLock_Response__Sequence__copy(
  const roomie_msgs__srv__ControlLock_Response__Sequence * input,
  roomie_msgs__srv__ControlLock_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__srv__ControlLock_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__srv__ControlLock_Response * data =
      (roomie_msgs__srv__ControlLock_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__srv__ControlLock_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__srv__ControlLock_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__srv__ControlLock_Response__copy(
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
// #include "roomie_msgs/srv/detail/control_lock__functions.h"

bool
roomie_msgs__srv__ControlLock_Event__init(roomie_msgs__srv__ControlLock_Event * msg)
{
  if (!msg) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__init(&msg->info)) {
    roomie_msgs__srv__ControlLock_Event__fini(msg);
    return false;
  }
  // request
  if (!roomie_msgs__srv__ControlLock_Request__Sequence__init(&msg->request, 0)) {
    roomie_msgs__srv__ControlLock_Event__fini(msg);
    return false;
  }
  // response
  if (!roomie_msgs__srv__ControlLock_Response__Sequence__init(&msg->response, 0)) {
    roomie_msgs__srv__ControlLock_Event__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__srv__ControlLock_Event__fini(roomie_msgs__srv__ControlLock_Event * msg)
{
  if (!msg) {
    return;
  }
  // info
  service_msgs__msg__ServiceEventInfo__fini(&msg->info);
  // request
  roomie_msgs__srv__ControlLock_Request__Sequence__fini(&msg->request);
  // response
  roomie_msgs__srv__ControlLock_Response__Sequence__fini(&msg->response);
}

bool
roomie_msgs__srv__ControlLock_Event__are_equal(const roomie_msgs__srv__ControlLock_Event * lhs, const roomie_msgs__srv__ControlLock_Event * rhs)
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
  if (!roomie_msgs__srv__ControlLock_Request__Sequence__are_equal(
      &(lhs->request), &(rhs->request)))
  {
    return false;
  }
  // response
  if (!roomie_msgs__srv__ControlLock_Response__Sequence__are_equal(
      &(lhs->response), &(rhs->response)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__srv__ControlLock_Event__copy(
  const roomie_msgs__srv__ControlLock_Event * input,
  roomie_msgs__srv__ControlLock_Event * output)
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
  if (!roomie_msgs__srv__ControlLock_Request__Sequence__copy(
      &(input->request), &(output->request)))
  {
    return false;
  }
  // response
  if (!roomie_msgs__srv__ControlLock_Response__Sequence__copy(
      &(input->response), &(output->response)))
  {
    return false;
  }
  return true;
}

roomie_msgs__srv__ControlLock_Event *
roomie_msgs__srv__ControlLock_Event__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ControlLock_Event * msg = (roomie_msgs__srv__ControlLock_Event *)allocator.allocate(sizeof(roomie_msgs__srv__ControlLock_Event), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__srv__ControlLock_Event));
  bool success = roomie_msgs__srv__ControlLock_Event__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__srv__ControlLock_Event__destroy(roomie_msgs__srv__ControlLock_Event * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__srv__ControlLock_Event__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__srv__ControlLock_Event__Sequence__init(roomie_msgs__srv__ControlLock_Event__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ControlLock_Event * data = NULL;

  if (size) {
    data = (roomie_msgs__srv__ControlLock_Event *)allocator.zero_allocate(size, sizeof(roomie_msgs__srv__ControlLock_Event), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__srv__ControlLock_Event__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__srv__ControlLock_Event__fini(&data[i - 1]);
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
roomie_msgs__srv__ControlLock_Event__Sequence__fini(roomie_msgs__srv__ControlLock_Event__Sequence * array)
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
      roomie_msgs__srv__ControlLock_Event__fini(&array->data[i]);
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

roomie_msgs__srv__ControlLock_Event__Sequence *
roomie_msgs__srv__ControlLock_Event__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__srv__ControlLock_Event__Sequence * array = (roomie_msgs__srv__ControlLock_Event__Sequence *)allocator.allocate(sizeof(roomie_msgs__srv__ControlLock_Event__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__srv__ControlLock_Event__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__srv__ControlLock_Event__Sequence__destroy(roomie_msgs__srv__ControlLock_Event__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__srv__ControlLock_Event__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__srv__ControlLock_Event__Sequence__are_equal(const roomie_msgs__srv__ControlLock_Event__Sequence * lhs, const roomie_msgs__srv__ControlLock_Event__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__srv__ControlLock_Event__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__srv__ControlLock_Event__Sequence__copy(
  const roomie_msgs__srv__ControlLock_Event__Sequence * input,
  roomie_msgs__srv__ControlLock_Event__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__srv__ControlLock_Event);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__srv__ControlLock_Event * data =
      (roomie_msgs__srv__ControlLock_Event *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__srv__ControlLock_Event__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__srv__ControlLock_Event__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__srv__ControlLock_Event__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
