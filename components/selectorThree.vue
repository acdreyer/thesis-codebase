<template>
  <el-select v-model="value" placeholder="Select">
    <el-option-group
      v-for="group in options"
      :key="group.label"
      :label="group.label">
      <el-option
        v-for="item in group.options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-option-group>
  </el-select>
</template>

<script>
  export default {
    data() {
      return {
        options: [{
          label: 'Famous Researchers',
          options: [{
            value: 'D. Prandtl',
            label: 'D. Prandtl'
          }, {
            value: 'H. Hoerner',
            label: 'H. Hoerner'
          }]
        }, {
          label: 'Notable Developments',
          options: [{
            value: 'Bell X-1 plane',
            label: 'ChenBell X-1 planegdu'
          }, {
            value: 'P-47 Thunderbolt',
            label: 'P-47 Thunderbolt'
          }, {
            value: 'B-17 Bomber',
            label: 'B-17 Bomber'
          }, {
            value: 'NACA airfoils',
            label: 'NACA airfoils'
          }]
        }],
        value: 'Notable Topics'
      }
    }
  }
</script>