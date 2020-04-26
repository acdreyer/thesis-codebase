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
          value: 'Research Memorandum	RM',
          label: 'Research Memorandum'
        }, {
          value: 'Technical Note	TN',
          label: 'Technical Note'
        }, {
          value: 'Technical Memorandum	TM',
          label: 'Technical Memorandum'
          }, {
            value: 'Technical Report	TR',
            label: 'Technical Report'
          }, {
            value: 'Wartime Reports	WR',
            label: 'Wartime Reports'
          }, {
            value: 'Aircraft Circular	AC',
            label: 'Aircraft Circular'
          }, {
          value: 'Memorandum Reports',
          label: 'Memorandum Reports'
          }, {
          value: 'Advance Restricted Reports	ARR',
          label: 'Advance Restricted Reports'
          }, {
          value: 'Advance Confidential Reports	ACR',
          label: 'Advance Confidential Reports'
        }],
        value: 'Document Type'
      }
    }
}
</script>

<style scoped>
@import url("//unpkg.com/element-ui@2.13.1/lib/theme-chalk/index.css");
</style>