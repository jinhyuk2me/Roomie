// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from roomie_msgs:msg/BatteryStatus.idl
// generated code does not contain a copyright notice

#include "roomie_msgs/msg/detail/battery_status__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__msg__BatteryStatus__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xa1, 0xfb, 0xfb, 0x6f, 0x21, 0x18, 0x86, 0xb9,
      0xb1, 0x5d, 0x2a, 0x67, 0x53, 0x19, 0x97, 0x02,
      0xbb, 0xe8, 0xd9, 0xbf, 0x42, 0x11, 0x92, 0xe7,
      0x9d, 0x9e, 0xf1, 0xcd, 0x10, 0x9a, 0x3e, 0x04,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char roomie_msgs__msg__BatteryStatus__TYPE_NAME[] = "roomie_msgs/msg/BatteryStatus";

// Define type names, field names, and default values
static char roomie_msgs__msg__BatteryStatus__FIELD_NAME__robot_id[] = "robot_id";
static char roomie_msgs__msg__BatteryStatus__FIELD_NAME__charge_percentage[] = "charge_percentage";
static char roomie_msgs__msg__BatteryStatus__FIELD_NAME__is_charging[] = "is_charging";

static rosidl_runtime_c__type_description__Field roomie_msgs__msg__BatteryStatus__FIELDS[] = {
  {
    {roomie_msgs__msg__BatteryStatus__FIELD_NAME__robot_id, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__msg__BatteryStatus__FIELD_NAME__charge_percentage, 17, 17},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__msg__BatteryStatus__FIELD_NAME__is_charging, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__msg__BatteryStatus__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__msg__BatteryStatus__TYPE_NAME, 29, 29},
      {roomie_msgs__msg__BatteryStatus__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# BatteryStatus.msg\n"
  "int32 robot_id\n"
  "float32 charge_percentage\n"
  "bool is_charging ";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__msg__BatteryStatus__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__msg__BatteryStatus__TYPE_NAME, 29, 29},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 78, 78},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__msg__BatteryStatus__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__msg__BatteryStatus__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
