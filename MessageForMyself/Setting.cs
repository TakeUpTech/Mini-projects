using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Setting : MonoBehaviour
{
    public GameObject settingCanvas, screenCanvas;
    private Animator settingAnim, screenAnim;
    public Message message;

    // Start is called before the first frame update
    void Start()
    {
        settingAnim = settingCanvas.GetComponent<Animator>();
        screenAnim = screenCanvas.GetComponent<Animator>();
    }

    public void OpenSetting(){
        settingAnim.SetBool("openSetting", true);
        screenAnim.SetBool("closeScreen", true);
    }

    public void CloseSetting(){
        settingAnim.SetBool("openSetting", false);
        screenAnim.SetBool("closeScreen", false);
    }

    public void ClearData(){
        PlayerPrefs.DeleteAll();
        message.ClearMessageList();
        // Debug.Log("Data removed.");
    }
}
