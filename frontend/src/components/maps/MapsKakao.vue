<template>
  <div class="maps-kakao">
    <form onsubmit="searchPlaces(); return false;">
      키워드 :
      <input type="text" value="금정역" id="keyword" size="15" >
      <button type="submit">검색하기</button>
    </form>
    <p id="result"></p>
    <div
      id="map"
      style="width: 70vw; height:70vh; position: inline-block; margin: 0 auto; padding: 0;"
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

      // 중심점 표시
      var marker = new kakao.maps.Marker({ position: map.getCenter() });
      marker.setMap(map);

      // 마커를 클릭했을 때 마커 위에 표시할 인포윈도우를 생성합니다
      var iwContent = '<div style="padding:5px;">Hello World!</div>'; // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다

      // 인포윈도우를 생성합니다
      var infowindow = new kakao.maps.InfoWindow({
        content: iwContent,
      });

      // 우측상단에 줌 막대 표시
      var control = new kakao.maps.ZoomControl();
      map.addControl(control, kakao.maps.ControlPosition.TOPRIGHT);

      var ps = new kakao.maps.services.Places();
      if (!!this.keyword === true) {
        ps.keywordSearch(this.keyword, placesSearchCB);
      }

      searchPlaces();

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
      kakao.maps.event.addListener(marker, "mouseover", function () {
        infowindow.open(map, marker);
      });

      // 마커에 마우스아웃 이벤트를 등록합니다
      kakao.maps.event.addListener(marker, "mouseout", function () {
        infowindow.close();
      });

      //////// KAKAOMAP FUNCTIONS ///////////////
      // 키워드 검색 완료 시 호출되는 콜백함수 입니다
      function placesSearchCB(data, status) {
        if (status === kakao.maps.services.Status.OK) {
          // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
          // LatLngBounds 객체에 좌표를 추가합니다
          var bounds = new kakao.maps.LatLngBounds();

          for (var i = 0; i < data.length; i++) {
            displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
          }
          // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
          map.setBounds(bounds);
        }
      }

      // 지도에 마커를 표시하는 함수입니다
      function displayMarker(place) {
        // 마커를 생성하고 지도에 표시합니다
        var marker = new kakao.maps.Marker({
          map: map,
          position: new kakao.maps.LatLng(place.y, place.x),
        });

        // 마커에 클릭이벤트를 등록합니다
        kakao.maps.event.addListener(marker, "click", function () {
          // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
          infowindow.setContent(
            '<div style="padding:5px;font-size:12px;">' +
              place.place_name +
              "</div>"
          );
          infowindow.open(map, marker);
        });
      }

      // 키워드 검색을 요청하는 함수
      function searchPlaces() {
        var keyword = document.getElementById('keyword').value;
        if (!keyword.replace(/^\s+|\s+$/g, "")) {
          alert("키워드를 입력해주세요!");
          return false;
        }
        // 장소검색 객체를 통해 키워드로 장소검색을 요청합니다
        ps.keywordSearch(keyword, placesSearchCB);
      }
    },
    addScript() {
      const script = document.createElement("script");
      /* global kakao */ script.onload = () => kakao.maps.load(this.initMap);
      const API_KEY = process.env.VUE_APP_KAKAO_MAP_KEY;
      script.src = `http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY}&libraries=services`;
      document.head.appendChild(script);
    },
  },
  data() {
    return {
      asdf: null,
      keyword: "강남역",
    };
  },
};
</script>

<style>
</style>