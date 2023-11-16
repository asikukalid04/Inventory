<%@ Page Title="" Language="C#" MasterPageFile="~/CLIENT.Master" AutoEventWireup="true" CodeBehind="CLIENT.aspx.cs" Inherits="NIRA.WebForm1" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
    <style type="text/css">
        .auto-style8 {
            color: #FFFFFF;
        background-color: #996633;
    }
        .auto-style9 {
            text-align: center;
        background-color: #996633;
    }
        .auto-style10 {
            width: 949px;
        background-color: #996633;
    }
        .auto-style11 {
        font-weight: bold;
        color: #FFFFFF;
        background-color: #996633;
    }
        .auto-style13 {
        background-color: #996633;
    }
    .auto-style15 {
        color: #000000;
    }
    .auto-style16 {
        font-weight: bold;
        color: #FFFFFF;
        height: 43px;
        background-color: #996633;
            width: 949px;
        }
    .auto-style17 {
        height: 43px;
        background-color: #996633;
    }
        .auto-style18 {
            font-weight: bold;
            color: #FFFFFF;
            background-color: #996633;
            width: 949px;
        }
    </style>
</asp:Content>
<asp:Content ID="Content3" ContentPlaceHolderID="ContentPlaceHolder2" runat="server">
    <table class="auto-style1">
        <tr>
            <td class="auto-style8" colspan="2" style="text-align: center"><strong>BIRTH REGISTRATION FORM</strong></td>
        </tr>
        <tr>
            <td class="auto-style18">BIRTH_NUMBER</td>
            <td class="auto-style13">
                <strong>
                <asp:TextBox ID="a" runat="server" Height="33px" Width="253px" CssClass="auto-style15"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style18">NAME</td>
            <td class="auto-style13">
                <strong>
                <asp:TextBox ID="b" runat="server" Height="33px" Width="253px" CssClass="auto-style15"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style18">GENDER</td>
            <td class="auto-style13">
                <strong>
                <asp:TextBox ID="c" runat="server" Height="33px" Width="253px" CssClass="auto-style15"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style18">DISTRICT</td>
            <td class="auto-style13">
                <strong>
                <asp:TextBox ID="d" runat="server" Height="33px" Width="253px" CssClass="auto-style15"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style18">NATIONALITY</td>
            <td class="auto-style13">
                <strong>
                <asp:TextBox ID="ee" runat="server" Height="33px" Width="253px" CssClass="auto-style15"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style18">DATE_OF_BIRTH</td>
            <td class="auto-style13">
                <strong>
                <asp:TextBox ID="f" runat="server" Height="33px" Width="253px" CssClass="auto-style15"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style16">PLACE_OF_BIRTH</td>
            <td class="auto-style17">
                <strong>
                <asp:TextBox ID="g" runat="server" Height="33px" Width="253px" CssClass="auto-style15"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style18">PLACE_OF_RESIDENCE</td>
            <td class="auto-style13">
                <strong>
                <asp:TextBox ID="h" runat="server" Height="33px" Width="253px" CssClass="auto-style15"></asp:TextBox>
                </strong>
            </td>
        </tr>
        <tr>
            <td class="auto-style11" colspan="2">&nbsp;</td>
        </tr>
        <tr>
            <td class="auto-style9" colspan="2"><span class="auto-style15">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span> <strong>&nbsp;<asp:Button ID="cmdsave" runat="server" CssClass="auto-style11" Height="35px" OnClick="cmdsave_Click" Text="SUBMIT" Width="99px" />
                <span class="auto-style8">&nbsp;&nbsp;&nbsp;&nbsp;
                </span>
                <asp:Button ID="cmdclr" runat="server" CssClass="auto-style11" Height="35px" OnClick="cmdclr_Click" Text="CLEAR" Width="99px" />
                <span class="auto-style8">&nbsp;&nbsp;&nbsp;&nbsp;
                </span>
                <asp:Button ID="cmddel" runat="server" CssClass="auto-style11" Height="35px" OnClick="cmddel_Click" Text="DELETE" Width="99px" />
                <span class="auto-style8">&nbsp;&nbsp;&nbsp;&nbsp;
                </span>
                <asp:Button ID="cmdupdate" runat="server" CssClass="auto-style11" Height="35px" OnClick="cmdupdate_Click" Text="UPDATE" Width="99px" />
                <span class="auto-style8">&nbsp;&nbsp;&nbsp;&nbsp;
                </span>
                <asp:Button ID="cmdupdate0" runat="server" CssClass="auto-style11" Height="35px" OnClick="cmdupdate0_Click" Text="VIEW DATA!" Width="99px" />
                </strong></td>
        </tr>
        <tr>
            <td class="auto-style9" colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <asp:Button ID="cmdsearch" runat="server" Height="34px" OnClick="cmdsearch_Click" Text="SEARCH" Width="100px" />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <asp:TextBox ID="aa" runat="server" Height="30px" Width="100px"></asp:TextBox>
            </td>
        </tr>
        <tr>
            <td class="auto-style9" colspan="2">
                <asp:Button ID="cmdsearch1" runat="server" Height="34px" OnClick="cmdsearch1_Click" Text="SEARCH" Width="100px" />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </td>
        </tr>
        <tr>
            <td class="auto-style10">
                <asp:GridView ID="GridView1" runat="server" style="color: #FFFFFF">
                </asp:GridView>
            </td>
            <td class="auto-style8">&nbsp;</td>
        </tr>
    </table>
</asp:Content>
