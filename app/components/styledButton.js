import React from "react";
import {View, Text, Pressable} from 'react-native';
import styles from '../screens/styles.js';

const StyledButton = (props) => {
    return(
        <View style={styles.container}>
            <Pressable style={styles.button}>
                <Text style={styles.text}>Login</Text>
            </Pressable>
        </View>
    );
};
const styles = StyleSheet.create({
    container: {
        width: '100%',
        padding: 10,
    },
    button:{
        height: 40,
        borderRadius: 20,
        alignItems: 'center',
        justifyContent: 'center',
    },
    text: {
        fontSize: 12,
        fontWeight: 'bold',
        textTransform: 'uppercase',
    },
});
export default StyledButton;