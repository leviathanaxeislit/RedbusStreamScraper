class RedBusInterfaceEnhancement:
    def create_card(self,bus):
        card_template = f"""
        <div style="background-color: #f9f9f9; padding: 10px; margin: 10px 0; border-radius: 10px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="flex: 1;">
                    <h4 style="color: #333; margin: 0;">{bus[1]}</h4>
                    <p style="margin: 0; font-size: 14px;">{bus[2]}</p>
                </div>
                <div style="text-align: right;">
                    <p style="margin: 0; font-size: 14px;"><strong>₹{bus[9]}</strong></p>
                    <p style="margin: 0; font-size: 12px;">⭐ {bus[8]}</p>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                <div>
                    <p style="margin: 0; font-size: 12px;"><strong>Departure:</strong> {bus[5]}</p>
                    <p style="margin: 0; font-size: 12px;"><strong>Arrival:</strong> {bus[7]}</p>
                </div>
                <div style="text-align: right;">
                    <p style="margin: 0; font-size: 12px;">🕒 {bus[6]}</p>
                    <p style="margin: 0; font-size: 12px;">🪑 {bus[10]} seats</p>
                </div>
            </div>
        </div>
        """
        return card_template