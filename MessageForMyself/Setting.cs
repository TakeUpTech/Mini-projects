using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Setting : MonoBehaviour
{
    public GameObject settingCanvas, screenCanvas;
    private Animator settingAnim, screenAnim;
    public Message message;

    // Start is called before the first frame update
    void Start() // Get animators of the menus to control their animations
    {
        settingAnim = settingCanvas.GetComponent<Animator>();
        screenAnim = screenCanvas.GetComponent<Animator>();
    }

    public void OpenSetting(){ // Allows to play the sliding animation of the menus
        settingAnim.SetBool("openSetting", true);
        screenAnim.SetBool("closeScreen", true);
    }

    public void CloseSetting(){ // Allows to play the sliding animation of the menus
        settingAnim.SetBool("openSetting", false);
        screenAnim.SetBool("closeScreen", false);
    }

    public void ClearData(){
        PlayerPrefs.DeleteAll(); // Remove all data save in the register thin PlayerPrefs functions
        message.ClearMessageList(); // Calls the function "ClearMessageList()" to delete all the elements of the message list
        // Debug.Log("Data removed.");
    }
}
