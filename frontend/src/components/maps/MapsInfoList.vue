<template>
  <table class="maps-info-list" >
    <thead>
      <tr>
        <th>이름</th>
        <th>분류</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in items" :key="item.name">
        <td>{{ item.name }}</td>
        <td>{{ item.type }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: "MapsInfoList",
  data() {
    return {
      items: [
        {
          name: "멀티 캠퍼스",
          type: "학원",
        },
        {
          name: "Starbucks",
          type: "카페",
        },
        {
          name: "HOLLYS coffee",
          type: "카페",
        },
        {
          name: "CU 편의점",
          type: "편의점",
        },
      ],
    };
  },
};
</script>

<style>
</style>