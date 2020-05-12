export interface vuelo{
    id ?: number;
    created_at ?: string;
    update_at ?: string;
    IdVuelo :string;
    Aerolinea : string;
    Estado1 : string;
    Estado2 ?: string;
    SiglasOrigen : number;
    Origen : string;
    HoraProgOrigen : string;
    HoraEstOrigen :string;
    TerminalOrigen : string;
    GateOrigen : string;
    SiglasDestino : string;
    Destino : string;
    HoraProgDestino : string;
    HoraEstDestino : string;
    TerminalDestino : string;
    GateDestino : string;
}