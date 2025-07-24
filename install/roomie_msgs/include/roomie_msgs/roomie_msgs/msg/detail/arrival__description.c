// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from roomie_msgs:msg/Arrival.idl
// generated code does not contain a copyright notice

#include "roomie_msgs/msg/detail/arrival__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__msg__Arrival__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x7c, 0xfd, 0x75, 0xa6, 0x6f, 0x7b, 0x3c, 0xf6,
      0xb1, 0x7a, 0x92, 0x47, 0xc7, 0x44, 0x20, 0xe8,
      0xdd, 0x45, 0x0a, 0xe2, 0x98, 0xb0, 0x19, 0xc2,
      0xd3, 0x06, 0x6b, 0xbb, 0x86, 0x99, 0x86, 0x37,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char roomie_msgs__msg__Arrival__TYPE_NAME[] = "roomie_msgs/msg/Arrival";

// Define type names, field names, and default values
static char roomie_msgs__msg__Arrival__FIELD_NAME__robot_id[] = "robot_id";
static char roomie_msgs__msg__Arrival__FIELD_NAME__task_id[] = "task_id";
static char roomie_msgs__msg__Arrival__FIELD_NAME__location_id[] = "location_id";

static rosidl_runtime_c__type_description__Field roomie_msgs__msg__Arrival__FIELDS[] = {
  {
    {roomie_msgs__msg__Arrival__FIELD_NAME__robot_id, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__msg__Arrival__FIELD_NAME__task_id, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__msg__Arrival__FIELD_NAME__location_id, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__msg__Arrival__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__msg__Arrival__TYPE_NAME, 23, 23},
      {roomie_msgs__msg__Arrival__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# Arrival.msg\n"
  "int32 robot_id\n"
  "int32 task_id\n"
  "int32 location_id\n"
  "\n"
  "# location_id values:\n"
  "# 0: LOB_WAITING\n"
  "# 1: LOB_CALL\n"
  "# 2: RES_PICKUP\n"
  "# 3: RES_CALL\n"
  "# 4: SUP_PICKUP\n"
  "# 5: ELE_1\n"
  "# 6: ELE_2\n"
  "# 101: ROOM_101 ";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__msg__Arrival__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__msg__Arrival__TYPE_NAME, 23, 23},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 199, 199},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__msg__Arrival__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__msg__Arrival__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
