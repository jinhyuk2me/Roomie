// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from roomie_msgs:msg/Arrival.idl
// generated code does not contain a copyright notice
#include "roomie_msgs/msg/detail/arrival__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
roomie_msgs__msg__Arrival__init(roomie_msgs__msg__Arrival * msg)
{
  if (!msg) {
    return false;
  }
  // robot_id
  // task_id
  // location_id
  return true;
}

void
roomie_msgs__msg__Arrival__fini(roomie_msgs__msg__Arrival * msg)
{
  if (!msg) {
    return;
  }
  // robot_id
  // task_id
  // location_id
}

bool
roomie_msgs__msg__Arrival__are_equal(const roomie_msgs__msg__Arrival * lhs, const roomie_msgs__msg__Arrival * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_id
  if (lhs->robot_id != rhs->robot_id) {
    return false;
  }
  // task_id
  if (lhs->task_id != rhs->task_id) {
    return false;
  }
  // location_id
  if (lhs->location_id != rhs->location_id) {
    return false;
  }
  return true;
}

bool
roomie_msgs__msg__Arrival__copy(
  const roomie_msgs__msg__Arrival * input,
  roomie_msgs__msg__Arrival * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // task_id
  output->task_id = input->task_id;
  // location_id
  output->location_id = input->location_id;
  return true;
}

roomie_msgs__msg__Arrival *
roomie_msgs__msg__Arrival__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__msg__Arrival * msg = (roomie_msgs__msg__Arrival *)allocator.allocate(sizeof(roomie_msgs__msg__Arrival), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__msg__Arrival));
  bool success = roomie_msgs__msg__Arrival__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__msg__Arrival__destroy(roomie_msgs__msg__Arrival * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__msg__Arrival__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__msg__Arrival__Sequence__init(roomie_msgs__msg__Arrival__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__msg__Arrival * data = NULL;

  if (size) {
    data = (roomie_msgs__msg__Arrival *)allocator.zero_allocate(size, sizeof(roomie_msgs__msg__Arrival), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__msg__Arrival__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__msg__Arrival__fini(&data[i - 1]);
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
roomie_msgs__msg__Arrival__Sequence__fini(roomie_msgs__msg__Arrival__Sequence * array)
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
      roomie_msgs__msg__Arrival__fini(&array->data[i]);
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

roomie_msgs__msg__Arrival__Sequence *
roomie_msgs__msg__Arrival__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__msg__Arrival__Sequence * array = (roomie_msgs__msg__Arrival__Sequence *)allocator.allocate(sizeof(roomie_msgs__msg__Arrival__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__msg__Arrival__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__msg__Arrival__Sequence__destroy(roomie_msgs__msg__Arrival__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__msg__Arrival__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__msg__Arrival__Sequence__are_equal(const roomie_msgs__msg__Arrival__Sequence * lhs, const roomie_msgs__msg__Arrival__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__msg__Arrival__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__msg__Arrival__Sequence__copy(
  const roomie_msgs__msg__Arrival__Sequence * input,
  roomie_msgs__msg__Arrival__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__msg__Arrival);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__msg__Arrival * data =
      (roomie_msgs__msg__Arrival *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__msg__Arrival__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__msg__Arrival__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__msg__Arrival__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
