<template>
  <el-select v-model="value" placeholder="Select">
    <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
  </el-select>
</template>


<script>
export default {
data() {
      return {
        options: [{
          value: '1. Aerodynamics',
          label: '1. Aerodynamics'
        }, {
          value: '2. Hydrodynamics',
          label: '2. Hydrodynamics'
        }, {
          value: '3. Propulsion',
          label: '3. Propulsion'
          }, {
            value: '4. Structures',
            label: '4. Structures'
          }, {
            value: '5. Operating Problems',
            label: '5. Operating Problems'
          }, {
            value: '6. Instruments',
            label: '6. Instruments'
          }, {
          value: '7. Research Equipment Techniques',
          label: '7. Research Equipment Techniques'
          }, {
          value: '8. Nomenclature,Bibliographies and Indexes',
          label: '8. Nomenclature,Bibliographies and Indexes'
          }, {
          value: '9. Technical Summaries',
          label: '9. Technical Summaries'
        }],
        value: 'Subject'
      }
    }
}
</script>

<style scoped>
@import url("//unpkg.com/element-ui@2.13.1/lib/theme-chalk/index.css");
</style>