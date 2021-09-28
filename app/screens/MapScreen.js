import React from "react";
import MapView from "react-native-maps";
import { Location, Permissions } from "expo";
import { View, Text, StyleSheet, Dimensions, TouchableOpacity } from "react-native";
import { Component } from "react";


const MapScreen = () => {
  let dataSpots;
  fetch('http://localhost/api/spots')
    .then(response => response.json())
    .then(data => dataSpots = data);

  return (
    <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
      <MapView style={styles.map}>


        <MapView.Marker
          key={2}
          coordinate={{ latitude: 57.035017, longitude: 9.946407 }}
          title={"test title"}
          description={"test descrip"}
        />

        {dataSpots => (
          <Marker
            key={index}
            coordinate={marker.latlng}
            title={marker.title}
            description={marker.description}
          />
        )}

      </MapView>

      <TouchableOpacity style={styles.overlay}>
        <Text style={styles.text}>Touchable Opacity</Text>
      </TouchableOpacity>
      <Text>Map Screen</Text>
    </View>
  );
};
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  map: {
    width: Dimensions.get("window").width,
    height: Dimensions.get("window").height,
  },
  overlay: {
    position: 'absolute',
    bottom: 50,
    backgroundColor: 'rgba(255, 255, 255, 1)',
  },
});
export default MapScreen;
