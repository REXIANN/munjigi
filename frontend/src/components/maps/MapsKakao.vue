<template>
  <div class="maps-kakao">
    <p id="result"></p>
    <div
      id="map"
      style="width: 70vw; height:90vh; position: inline-block; margin: 0 auto; padding: 0;"
    ></div>
  </div>
</template>

<script >
export default {
  name: "MapsKakao",
  mounted() {
    window.kakao && window.kakao.maps ? this.initMap() : this.addScript();
  },
  computed: {},
  methods: {
    initMap() {
      var container = document.getElementById("map");
      var options = {
        center: new kakao.maps.LatLng(37.501276, 127.039642),
        level: 3,
      };
      // 지도 표시
      var map = new kakao.maps.Map(container, options);
      this.map = map;
      
      // 중심점 표시
      var marker = new kakao.maps.Marker({ position: map.getCenter() });
      this.marker = marker;
      marker.setMap(map);

      // 마커를 클릭했을 때 마커 위에 표시할 인포윈도우를 생성합니다
      var iwContent = '<div style="padding:5px;">Hello World!</div>' // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다

      // 인포윈도우를 생성합니다
      var infowindow = new kakao.maps.InfoWindow({
        content: iwContent
      });

      // 우측상단에 줌 막대 표시
      var control = new kakao.maps.ZoomControl();
      map.addControl(control, kakao.maps.ControlPosition.TOPRIGHT);


      ////////KAKAOMAP EVENT LISTENERS/////////////////////
      // 맵의 중심이 바뀌는 경우 동작
      kakao.maps.event.addListener(map, "center_changed", function () {
        // var level = map.getLevel();
        var latlng = map.getCenter();

        var message =
          "중심 좌표: 위도:" + latlng.getLat() + ", 경도 " + latlng.getLng();
        var resultDiv = document.getElementById("result");
        resultDiv.innerHTML = message;
      });

      // 좌측하단 타일로드 표시
      kakao.maps.event.addListener(map, "tilesloaded", function () {
        marker.setPosition(map.getCenter());
        marker.setMap(map);
      });
      
      // 마커에 마우스오버 이벤트를 등록합니다
      kakao.maps.event.addListener(marker, 'mouseover', function() {
        // 마커에 마우스오버 이벤트가 발생하면 인포윈도우를 마커위에 표시합니다
          infowindow.open(map, marker);
      });

      // 마커에 마우스아웃 이벤트를 등록합니다
      kakao.maps.event.addListener(marker, 'mouseout', function() {
          // 마커에 마우스아웃 이벤트가 발생하면 인포윈도우를 제거합니다
          infowindow.close();
      });
      
    },
    addScript() {
      const script = document.createElement("script");
      /* global kakao */ script.onload = () => kakao.maps.load(this.initMap);
      const API_KEY = process.env.VUE_APP_KAKAO_MAP_KEY;
      script.src = `http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY}`;
      document.head.appendChild(script);
    },
  },
  data() {
    return {
      map: null,
      level: null,
      lat: null,
      lng: null,
      marker: null,
      geocoder: null,
    };
  },
};
</script>

<style>
</style>