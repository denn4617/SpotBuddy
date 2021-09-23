import React from "react";
import MapView from "react-native-maps";
import { Location, Permissions } from "expo";
import { View, Text, StyleSheet, Dimensions, Button } from "react-native";
import { Component } from "react";

const NotificationScreen = () => {
  return (
    <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
      <MapView
        style={styles.map}
      // region={{
      //   latitude: 37.78,
      //   longitude: -122.43,
      //   latitudeDelta: 0.015,
      //   longitudeDelta: 0.0121,
      // }}
      >
        <MapView.Marker
          key={2}
          coordinate={{ latitude: 57.035017, longitude: 9.946407 }}
          title={"test title"}
          description={"test descrip"}
        />

      </MapView>

      <Text>Notification Screen</Text>
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
});
export default NotificationScreen;
