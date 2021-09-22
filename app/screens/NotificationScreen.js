import React from "react";
import MapView from "react-native-maps";
import { View, Text, StyleSheet, Dimensions } from "react-native";

const NotificationScreen = () => {
  return (
    <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
      <MapView style={styles.map} />
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
